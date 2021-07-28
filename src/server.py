from concurrent import futures
from google.protobuf.json_format import MessageToDict


import logging

import grpc

import pedido_pb2
import pedido_pb2_grpc


produtos = [
    {'id': '1', 'nome': 'Tinta', 'preco': 10.85, 'quantidade': 10},
    {'id': '2', 'nome': 'Tubos', 'preco': 13.00, 'quantidade': 15},
    {'id': '3', 'nome': 'Interruptor', 'preco': 9.50, 'quantidade': 17},
    {'id': '4', 'nome': 'Cabos', 'preco': 15.00, 'quantidade': 18},
    {'id': '5', 'nome': 'Furadeira', 'preco': 29.90, 'quantidade': 5},
    {'id': '6', 'nome': 'Lampadas', 'preco': 16.90, 'quantidade': 18},
    {'id': '7', 'nome': 'Pregos', 'preco': 5.45, 'quantidade': 40},
    {'id': '8', 'nome': 'Alicate', 'preco': 14.00, 'quantidade': 8},
    {'id': '9', 'nome': 'Martelo', 'preco': 13.75, 'quantidade': 9},
    {'id': '10', 'nome': 'Madeira', 'preco': 19.00, 'quantidade': 12},
]

pedidos = []


class ProdutosService(pedido_pb2_grpc.ProdutoServiceServicer):
    def List(self, request, context):
        return pedido_pb2.ProdutoList(produtos=produtos)

    def Pedido(self, request, context):
        pedido = MessageToDict(request)
        status = ''
        msg = ''
        preco = 0

        for produto in pedido['idProdutos']:
            produto_id = produto['id']
            produto_quantidade = produto['quantidade']
            for p in produtos:
                if p['id'] == produto_id:
                    if produto_quantidade > p['quantidade']:
                        status = 'Failed'
                        msg = 'Compra cancelada! Itens adicionados excedem o estoque'

                        return pedido_pb2.PedidoResponse(status=status, msg=msg)

        itens = []
        for produto in pedido['idProdutos']:
            for p in produtos:
                if p['id'] == produto_id:
                    preco += p['preco'] * produto_quantidade
                    itens.append(p)
                    p['quantidade'] -= produto_quantidade

        preco = round(preco, 2)
        status = 'Aproved'
        msg = 'Compra concluida!'

        pedidos.append({
            'status': status,
            'msg': msg,
            'preco': preco,
            'itens': itens
        })

        return pedido_pb2.PedidoResponse(status=status, msg=msg, preco=preco)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pedido_pb2_grpc.add_ProdutoServiceServicer_to_server(
        ProdutosService(), server
    )
    server.add_insecure_port("[::]:8080")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
