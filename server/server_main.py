#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('C:/Users/Administrator/PycharmProjects/testkeras')
import grpc
import time
from concurrent import futures
from example import data_pb2
from example import data_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = "0.0.0.0"
_PORT = "19999"

class HelloWorld(data_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("request: " + str(request))
        return data_pb2.HelloReply(name='sunzhi',message= str(request.message).upper() ,location='%s, %s!' % (request.message, str(int(request.ip) + 100)))

def server():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    data_pb2_grpc.add_GreeterServicer_to_server(HelloWorld(), grpcServer)
    grpcServer.add_insecure_port("{0}:{1}".format(_HOST, _PORT))
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    server()