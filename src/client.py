from __future__ import print_function
from google.protobuf.json_format import MessageToDict

from utils import clear

import logging

import grpc

import pedido_pb2
import pedido_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = pedido_pb2_grpc.ProdutoServiceStub(channel)

        list_produtos(stub)
        items_pedido(stub)


def list_produtos(stub):
    response_list_produtos = stub.List(pedido_pb2.Void())
    list_produtos = MessageToDict(response_list_produtos)

    clear()
    print('Produtos disponíveis:')
    print('{:<6} {}'.format('ID', 'Produto'))
    print('--'*10)
    for produto in list_produtos['produtos']:
        print('{:<6} {}'.format(produto['id'], produto['nome']))
    print('--'*10)


def items_pedido(stub):
    print('Digite 0 para finalizar lista.')
    print('Digite o ID do produto e a quantidade que deseja.')
    pedido = []
    user_input = input()
    while user_input != '0':
        produto_id, quantidade = map(str, user_input.split())

        pedido.append(pedido_pb2.PedidoProduto(
            id=produto_id, quantidade=int(quantidade)))

        user_input = input()

    response_pedido = stub.Pedido(pedido_pb2.PedidoList(id_produtos=pedido))

    clear()
    print(response_pedido)


if __name__ == '__main__':
    logging.basicConfig()
    run()
