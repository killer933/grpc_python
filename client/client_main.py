#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('C:/Users/Administrator/PycharmProjects/testkeras')
import grpc

from example import data_pb2
from example import data_pb2_grpc
import time
_HOST = '127.0.0.1'
_PORT = '19999'


def run():
    with grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT)) as channel:
        client = data_pb2_grpc.GreeterStub(channel=channel)
        for i in range(3):
            time.sleep(1)
            response = client.SayHello(data_pb2.HelloRequest(name='you', message='hey guys: ' + str(i),ip=str(i)))
            print(str(i) +"  received: " + response.message)
        print(response)

if __name__ == '__main__':
    run()
# channel = grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT))
# client = data_pb2_grpc.GreeterStub(channel=channel)
# response = client.SayHello(data_pb2.HelloRequest(name='you', message='hey guys'))
# print("received: " + response.message)