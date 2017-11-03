"""
Simple Collector, accept gNMI calls from test client and initiate new gNMI calls
to Probes. Behaves as gNMI server to the test client and gNMI client to the probes
"""

import gnmi.gnmi_pb2_grpc as gnmi_pb2_grpc
import gnmi.gnmi_pb2 as gnmi_pb2
#from pathtree.pathtree import Branch as Branch 
#from pathtree.pathtree import Path
import grpc
from concurrent import futures
import time
import logging
import argparse
import Queue
import p4.p4_pb2 as p4_pb2
import math
from google.protobuf import any_pb2
from google.protobuf import message
from google.protobuf.json_format import MessageToJson

# - logging configuration
logging.basicConfig()
logger = logging.getLogger('collector')

logger.setLevel(logging.DEBUG)

#configure southbound device address
device_ip = "localhost"
device_port = 80049
host_ip = "localhost"
host_port = 80050

interval = 1

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

queues = []


class CollectorServicer(gnmi_pb2_grpc.gNMIServicer):

    def __init__(self):
        #initiate an empty pathtree for storing updates from the probes
        #self.ptree = Branch() 
        pass
    def Subscribe(self, request_iterator, context):
        #create a channel connecting to the southbound device
        channel = grpc.insecure_channel(device_ip + ":" + str(device_port))
        stub = gnmi_pb2.gNMIStub(channel)
        counter = 0
        global interval
        eventQ = Queue.Queue()
        ptime = time.time()
        #start streaming
        for response in stub.Subscribe(request_iterator):
            #logger.debug(response)
            path =""
            for update in response.update.update:
                event = p4_pb2.P4_int()
                update.val.any_val.Unpack(event)
                eventQ.put(event)
                path = update.path
            else:
                pass
            ctime = time.time()
            if(ctime - ptime >= interval):
                eventlist = []
                while not eventQ.empty():
                    eventlist.append(eventQ.get())
                if len(eventlist) > 0: 
                    for e in eventlist:
                        jsonObj = MessageToJson(e)
                        #logger.debug(jsonObj)
                    aggregated = self.processQ(eventlist)
                    logger.debug("aggregatedTo: %s" %(MessageToJson(aggregated)))
                    any_msg = any_pb2.Any()
                    any_msg.Pack(aggregated)
                    typedValue = gnmi_pb2.TypedValue(any_val=any_msg)
                    a_update = gnmi_pb2.Update(path=path, val=typedValue)
                    a_updates = []
                    a_updates.append(a_update)
                    a_noti = gnmi_pb2.Notification(timestamp=response.update.timestamp, update=a_updates)
                    yield gnmi_pb2.SubscribeResponse(update=a_noti) 
                ptime = time.time()

        print "Streaming done!"

    def processQ(self, eventlist):
       
        base = p4_pb2.P4_int()
        for event in eventlist:
            base.switch_id = max(base.switch_id, event.switch_id)
            base.version = max(base.version, event.version)
            base.replication = max(base.replication, event.replication)
            base.c = max(base.c, event.c)
            base.hop_count_exceeded = max(base.hop_count_exceeded, event.hop_count_exceeded)
            base.inst_count = max(base.inst_count, event.inst_count)
            base.Max_hop_count = max(base.Max_hop_count, event.Max_hop_count)
            base.p4_int_metadata.extend(event.p4_int_metadata)
        self.mergeKpis(base)

        return base
    def mergeKpis (self, event):
        dic = {}
        for e in event.p4_int_metadata:
            if (e.type, e.switch_id, e.item_id) in dic:
                base = dic[e.type, e.switch_id, e.item_id][0]
                base.c_plane_state_ver_number = base.c_plane_state_ver_number+e.c_plane_state_ver_number
                base.timestamp = max(base.timestamp, e.timestamp)
                dic[e.type,e.switch_id,e.item_id][1] = dic[e.type,e.switch_id,e.item_id][1]+1
                
                for k, v in e.kpis.iteritems():
                    if k in base.kpis:
                        base.kpis[k] = base.kpis[k] + v
                    else:
                        base.kpis[k] = v
            else:
                dic[e.type, e.switch_id, e.item_id] = [e, 1]
        aggregated = []
        for key in dic:
            for kpi, value in dic[key][0].kpis.items():
                dic[key][0].kpis[kpi] = dic[key][0].kpis[kpi]/dic[key][1]
            aggregated.append(dic[key][0])

        del event.p4_int_metadata[:]
        event.p4_int_metadata.extend(aggregated)

    def encodePath(self, path):
        pathStrs = []
        for pe in path:
            pstr = pe.name
            if pe.key:
                for k, v in pe.key.iteritems():
                    pstr += "[" + str(k) + "=" + str(v) + "]"
            pathStrs.append(pstr)
        return pathStrs


def serve():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost',
                        help='OpenConfig server host')
    parser.add_argument('--port', type=int, default=80050,
                        help='OpenConfig server port')
    parser.add_argument('--device_port', type=int, default=80049,
                        help='OpenConfig device port')
    parser.add_argument('--sample', type=int, default=1,
                        help='how many messages to be aggregated')
    parser.add_argument('--debug', type=str, default='on', help='debug level')
    args = parser.parse_args()

    global device_port
    global interval
    device_port = args.device_port
    interval = args.sample

    if args.debug == "off":
        logger.setLevel(logging.INFO)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gnmi_pb2_grpc.add_gNMIServicer_to_server(
        CollectorServicer(), server)
    server.add_insecure_port(args.host + ":" + str(args.port))
    server.start()
    logger.info("Collector Server Started.....")
    try:
       while True:
          time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
