#!/usr/bin/env python
"""
gNMI server to simulate a fake probe

"""
import grpc
import gnmi.gnmi_pb2 as gnmi_pb2
import gnmi.gnmi_pb2_grpc as gnmi_pb2_grpc
from concurrent import futures
import time
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
port=80049

#gNMI service which provides all rpc calls for gNMI client 
class ProbeServicer(gnmi_pb2_grpc.gNMIServicer):
    def __init__(self):
       # createStreams()
       pass

    def createStreams():
        pass

    def fakeValue(self, path):
        val = (randint(0,100))
        encoding_type = 1 
        tm = int(time.time() * 1000) 
        #value = gnmi_pb2.Value(value=val, type=encoding_type)
        typedValue = gnmi_pb2.TypedValue(int_val=val)
        return gnmi_pb2.Update(path=path,val=typedValue)

    def Subscribe(self, request_iterator, context):
        
        tag = 0
        for request in request_iterator:
            sublist = request.subscribe.subscription
            mode = request.subscribe.mode 
             
            while(1):
                update_msg = []
                for sub in sublist:
                    update_msg.append(self.fakeValue(sub.path))
                tm = int(time.time() * 1000)
                noti = gnmi_pb2.Notification(timestamp=tm, update=update_msg)
                time.sleep(1)
                logger.info("Generate new update : " )
                logger.info(noti)
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
  args = parser.parse_args()

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
