# Copyright (C) 2016  Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

"""Common resources used by gRPC OpenConfig clients and servers."""

import pyopenconfig.gnmi_pb2


def make_path(path_str):
    """Create a Path object from a string path"""
    element = path_str.split('/')
    path = pyopenconfig.gnmi_pb2.Path(element=element)
    return path


def make_get_request(path_str='/'):
    """Create a subscribe request from a string path"""
    path = make_path(path_str)
    return pyopenconfig.gnmi_pb2.GetRequest(path=[path])


def make_subscribe_request(path_str='/', mode='stream'):
    """Create a subscribe request from a string path"""
    path = make_path(path_str)
    subscription = pyopenconfig.gnmi_pb2.Subscription(path=path)
    if mode == "once":
        mode = 1
    elif mode == "poll":
        mode = 2
    else:
        mode = 0
    subscription_list = pyopenconfig.gnmi_pb2.SubscriptionList(subscription=[subscription],mode=mode)
    yield pyopenconfig.gnmi_pb2.SubscribeRequest(subscribe=subscription_list)
