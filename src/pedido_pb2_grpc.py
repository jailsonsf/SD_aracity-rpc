# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pedido_pb2 as pedido__pb2


class ProdutoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/ProdutoService/List',
                request_serializer=pedido__pb2.Void.SerializeToString,
                response_deserializer=pedido__pb2.ProdutoList.FromString,
                )
        self.Pedido = channel.unary_unary(
                '/ProdutoService/Pedido',
                request_serializer=pedido__pb2.PedidoList.SerializeToString,
                response_deserializer=pedido__pb2.PedidoResponse.FromString,
                )


class ProdutoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pedido(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProdutoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=pedido__pb2.Void.FromString,
                    response_serializer=pedido__pb2.ProdutoList.SerializeToString,
            ),
            'Pedido': grpc.unary_unary_rpc_method_handler(
                    servicer.Pedido,
                    request_deserializer=pedido__pb2.PedidoList.FromString,
                    response_serializer=pedido__pb2.PedidoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProdutoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProdutoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProdutoService/List',
            pedido__pb2.Void.SerializeToString,
            pedido__pb2.ProdutoList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pedido(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProdutoService/Pedido',
            pedido__pb2.PedidoList.SerializeToString,
            pedido__pb2.PedidoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
