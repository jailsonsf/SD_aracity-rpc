from __future__ import print_function
import logging

import grpc

import pedido_pb2
import pedido_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = pedido_pb2_grpc.ProdutoServiceStub(channel)
        response = stub.List(pedido_pb2.Void())

    print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
