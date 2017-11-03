#!/usr/bin/env python
# Copyright (C) 2016  Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

"""The Python implementation of a gNMI client."""

from __future__ import print_function

import argparse
import logging
import sys
import time

import grpc
import grpc.framework.interfaces.face
import pyopenconfig.gnmi_pb2
import pyopenconfig.resources
import p4.p4_pb2 as p4_pb2

import potsdb
import atexit
from influxdb import InfluxDBClient

# - logging configuration
logging.basicConfig()
logger = logging.getLogger('test-client')

logger.setLevel(logging.DEBUG)

host_ip = "localhost"
host_port = 80050

mode = "stream"
nums = 0

db_host = '127.0.0.1'
#db_port = 8086
db_port = 4242
metrics = potsdb.Client(db_host, port=db_port)
#client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
#client.create_database('example')


def encodePath(path):
    pathStrs = "" 
    for pe in path:
        pstr = pe.name
        if pe.key:
             for k, v in pe.key.iteritems():
                  pstr += "[" + str(k) + "=" + str(v) + "]"
        pathStrs = pathStrs + "." + pstr
    return pathStrs[1:]

def mapToJson(k,v,data):
    if (data.type == 0):
        dtype = "ingress"
    elif (data.type == 1):
        dtype = "egress"
    else:
        dtype = "buffer"
    d = {}
    d["measurement"] = k
    d["tags"] ={"switch_id":data.switch_id,"item_id":data.item_id,"type":dtype}
    d["time"] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(data.timestamp)) 
    d["fields"] = {"value":v}
    return [d]

def saveToOPTSDB(event):

    for data in event.p4_int_metadata:
            for k, v in data.kpis.iteritems():
               # tm = data.timestamp
                tm = time.time()
               # json_body = mapToJson(k,v,data)
               # client.write_points(json_body)
                if (data.type == 0):
                     dtype = "ingress"
                elif (data.type == 1):
                     dtype = "egress"
                else:
                     dtype = "buffer"
                metrics.send(k,v,timestamp=tm,switch_id=data.switch_id,item_id=data.item_id,type=dtype)
                logger.debug("send to TSDB: k:%s, v:%s, tag1:%s, tag2:%s, tag3:%s" %(k,v,data.switch_id,data.item_id,data.type))

def saveToTSDB(event):

    for data in event.p4_int_metadata:
            for k, v in data.kpis.iteritems():
                tm = data.timestamp
                json_body = mapToJson(k,v,data)
                client.write_points(json_body)
                logger.debug("send to TSDB: k:%s, v:%s, switch_id:%s, item_id:%s, type:%s" %(k,v,data.switch_id,data.item_id,data.type))

 
def get(stub, path_str, metadata):
    """Get and echo the response"""
    response = stub.Get(pyopenconfig.resources.make_get_request(path_str),
                        metadata=metadata)
    print(response)

def subscribe(stub, path_str, mode, metadata):
    global nums
    """Subscribe and echo the stream"""
    logger.info("start to subscrib path: %s in %s mode" % (path_str, mode))
    subscribe_request = pyopenconfig.resources.make_subscribe_request(path_str=path_str, mode=mode)
    i = 0
    try:
        for response in stub.Subscribe(subscribe_request, metadata=metadata):
            #logger.debug(response)
            p4 = p4_pb2.P4_int()
            for update in response.update.update:
              update.val.any_val.Unpack(p4)
              saveToOPTSDB(p4)
            i += 1
            nums = i
    except grpc.framework.interfaces.face.face.AbortionError, error: # pylint: disable=catching-non-exception
        if error.code == grpc.StatusCode.OUT_OF_RANGE and error.details == 'EOF':
            # https://github.com/grpc/grpc/issues/7192
            sys.stderr.write('EOF after %d updates\n' % i)
            logger.info('EOF after %d updates\n' % i)
        else:
            raise

    logger.info("Finished streaming, %s updates has been streamed." % i)

def shutdown_hook():
    global nums
    try:
        pass
    except Exception:
        pass 
    finally:
        logger.info("%s updates has been streamed." % nums)
        logger.info('existing program')


def run():
    """Main loop"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost',
                        help='OpenConfig server host')
    parser.add_argument('--port', type=int, default=80051,
                        help='OpenConfig server port')
    parser.add_argument('--username', type=str, help='username')
    parser.add_argument('--password', type=str, help='password')
    parser.add_argument('--mode', type=str, default='stream', help='subscription mode')
    parser.add_argument('--debug', type=str, default='on', help='debug level')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--get',
                       help='OpenConfig path to perform a single-shot get')
    group.add_argument('--subscribe',
                       help='OpenConfig path to subscribe to')
    args = parser.parse_args()

    metadata = None
    if args.debug == "off":
        logger.setLevel(logging.INFO)
        
    if args.username or args.password:
        metadata = [("username", args.username), ("password", args.password)]

    channel = grpc.insecure_channel(args.host + ":" + str(args.port))
    stub = pyopenconfig.gnmi_pb2.gNMIStub(channel)

    atexit.register(shutdown_hook) 

    if args.get:
        get(stub, args.get, metadata)
    elif args.subscribe:
        subscribe(stub, args.subscribe, args.mode, metadata)
    else:
        subscribe(stub, '/', metadata)


if __name__ == '__main__':
    run()
