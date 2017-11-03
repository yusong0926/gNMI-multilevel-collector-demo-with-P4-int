#!/usr/bin/env python
"""
gNMI server to simulate a fake probe
"""
import grpc
import gnmi.gnmi_pb2 as gnmi_pb2
import gnmi.gnmi_pb2_grpc as gnmi_pb2_grpc
import p4.p4_pb2 as p4_pb2
from google.protobuf.json_format import MessageToJson
from google.protobuf import any_pb2
from concurrent import futures
import time
import thread
import datetime
from random import randint
import argparse
import logging

# - logging configuration
logging.basicConfig()
logger = logging.getLogger('probe')

logger.setLevel(logging.DEBUG)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

host='localhost'
port=7000
time_frequency = 1.0
fd = "p4.csv"

#gNMI service which provides all rpc calls for gNMI client 
class ProbeServicer(gnmi_pb2_grpc.gNMIServicer):
    def __init__(self):
        self.model = p4_pb2.P4_int()
        self.createStreams()

    def createStreams(self):
        thread.start_new_thread(self.updateModel, ("tn", fd))

    def updateModel(self, treadname, fd):
        while True:
         time.sleep(1)
         self.model.switch_id = 1 
         self.model.version = (randint(0,10)) 
         self.model.replication = (randint(0,10)) 
         self.model.c = (randint(0,10)) 
         self.model.hop_count_exceeded = (randint(0,100)) 
         self.model.inst_count = (randint(0,100)) 
         self.model.Max_hop_count = (randint(0,100)) 
         kpimap1 = {"port_pkt_count":randint(0,100), "port_byte_count":randint(0,100),"port_drop_count":randint(0,100),"port_utilization":randint(0,100)}
         kpimap2 = {"port_pkt_count":randint(0,100), "port_byte_count":randint(0,100),"port_drop_count":randint(0,100),"port_utilization":randint(0,100)}
         kpimap3 = {"inst_queue_len":randint(0,100), "avg_queue_len":randint(0,100),"congestion_status":randint(0,100),"queue_drop_count":randint(0,100)}
         sid = randint(1,5)
         metadata1 = p4_pb2.P4_int_metadata(type=0, timestamp=int(time.time()), switch_id=sid,item_id=randint(1,10),kpis= kpimap1)
         metadata2 = p4_pb2.P4_int_metadata(type=1,timestamp=int(time.time()),switch_id=sid,item_id=randint(1,10),kpis= kpimap2)
         metadata3 = p4_pb2.P4_int_metadata(type=2,timestamp=int(time.time()),switch_id=sid,item_id=randint(1,10),kpis= kpimap3)
         sid = randint(1,5)
         metadata4 = p4_pb2.P4_int_metadata(type=0, timestamp=int(time.time()), switch_id=sid,item_id=randint(1,10),kpis= kpimap1)
         metadata5 = p4_pb2.P4_int_metadata(type=1,timestamp=int(time.time()),switch_id=sid,item_id=randint(1,10),kpis= kpimap2)
         metadata6 = p4_pb2.P4_int_metadata(type=2,timestamp=int(time.time()),switch_id=sid,item_id=randint(1,10),kpis= kpimap3)
         del self.model.p4_int_metadata[:]
         self.model.p4_int_metadata.extend([metadata1, metadata2, metadata3, metadata4,metadata5,metadata6])

    def probeValue(self, path):
        any_msg = any_pb2.Any()
        any_msg.Pack(self.model)
        typedValue = gnmi_pb2.TypedValue(any_val=any_msg)
        logger.debug(MessageToJson(self.model))
        return gnmi_pb2.Update(path=path, val=typedValue) 

    def Subscribe(self, request_iterator, context):
        
        tag = 0
        for request in request_iterator:
            sublist = request.subscribe.subscription
            mode = request.subscribe.mode 
             
            while(1):
                update_msg = []
                for sub in sublist:
                    update_msg.append(self.probeValue(sub.path))
                tm = int(time.time() * 1000)
                noti = gnmi_pb2.Notification(timestamp=tm, update=update_msg)
                #time.sleep(time_frequency)
                yield gnmi_pb2.SubscribeResponse(update=noti)
                if mode == 0:
                    continue
                else:
                    break
            if mode == 1:
                break
            print "waiting for new request"

        print "Streaming done: close channel"

def serve():
  parser = argparse.ArgumentParser()
  parser.add_argument('--host', default='localhost',help='OpenConfig server host')
  parser.add_argument('--port', default=80049,help='OpenConfig server port')
  parser.add_argument('--time', default=1,help='data generating frequency')
  parser.add_argument('--debug', type=str, default='on', help='debug level')
  args = parser.parse_args()

  global time_frequency
  time_frequency = float(args.time)

  if args.debug == "off":
       logger.setLevel(logging.INFO)

  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  gnmi_pb2_grpc.add_gNMIServicer_to_server(
      ProbeServicer(), server)
  server.add_insecure_port(args.host + ":" + str(args.port))
  server.start()
  print "Probe Server Started...."
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
