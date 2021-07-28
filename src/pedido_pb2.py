# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pedido.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pedido.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cpedido.proto\"\x06\n\x04Void\",\n\x0ePedidoResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x17\n\tProdutoId\x12\n\n\x02id\x18\x01 \x01(\t\"F\n\x07Produto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\r\n\x05preco\x18\x03 \x01(\x02\x12\x12\n\nquantidade\x18\x04 \x01(\x05\")\n\x0bProdutoList\x12\x1a\n\x08produtos\x18\x01 \x03(\x0b\x32\x08.Produto2-\n\x0eProdutoService\x12\x1b\n\x04List\x12\x05.Void\x1a\x0c.ProdutoList28\n\rPedidoService\x12\'\n\x06Pedido\x12\x0c.ProdutoList\x1a\x0f.PedidoResponseb\x06proto3'
)




_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=22,
)


_PEDIDORESPONSE = _descriptor.Descriptor(
  name='PedidoResponse',
  full_name='PedidoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PedidoResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='PedidoResponse.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=68,
)


_PRODUTOID = _descriptor.Descriptor(
  name='ProdutoId',
  full_name='ProdutoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ProdutoId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=93,
)


_PRODUTO = _descriptor.Descriptor(
  name='Produto',
  full_name='Produto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Produto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nome', full_name='Produto.nome', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preco', full_name='Produto.preco', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantidade', full_name='Produto.quantidade', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=165,
)


_PRODUTOLIST = _descriptor.Descriptor(
  name='ProdutoList',
  full_name='ProdutoList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='produtos', full_name='ProdutoList.produtos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=208,
)

_PRODUTOLIST.fields_by_name['produtos'].message_type = _PRODUTO
DESCRIPTOR.message_types_by_name['Void'] = _VOID
DESCRIPTOR.message_types_by_name['PedidoResponse'] = _PEDIDORESPONSE
DESCRIPTOR.message_types_by_name['ProdutoId'] = _PRODUTOID
DESCRIPTOR.message_types_by_name['Produto'] = _PRODUTO
DESCRIPTOR.message_types_by_name['ProdutoList'] = _PRODUTOLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'pedido_pb2'
  # @@protoc_insertion_point(class_scope:Void)
  })
_sym_db.RegisterMessage(Void)

PedidoResponse = _reflection.GeneratedProtocolMessageType('PedidoResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEDIDORESPONSE,
  '__module__' : 'pedido_pb2'
  # @@protoc_insertion_point(class_scope:PedidoResponse)
  })
_sym_db.RegisterMessage(PedidoResponse)

ProdutoId = _reflection.GeneratedProtocolMessageType('ProdutoId', (_message.Message,), {
  'DESCRIPTOR' : _PRODUTOID,
  '__module__' : 'pedido_pb2'
  # @@protoc_insertion_point(class_scope:ProdutoId)
  })
_sym_db.RegisterMessage(ProdutoId)

Produto = _reflection.GeneratedProtocolMessageType('Produto', (_message.Message,), {
  'DESCRIPTOR' : _PRODUTO,
  '__module__' : 'pedido_pb2'
  # @@protoc_insertion_point(class_scope:Produto)
  })
_sym_db.RegisterMessage(Produto)

ProdutoList = _reflection.GeneratedProtocolMessageType('ProdutoList', (_message.Message,), {
  'DESCRIPTOR' : _PRODUTOLIST,
  '__module__' : 'pedido_pb2'
  # @@protoc_insertion_point(class_scope:ProdutoList)
  })
_sym_db.RegisterMessage(ProdutoList)



_PRODUTOSERVICE = _descriptor.ServiceDescriptor(
  name='ProdutoService',
  full_name='ProdutoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=210,
  serialized_end=255,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='ProdutoService.List',
    index=0,
    containing_service=None,
    input_type=_VOID,
    output_type=_PRODUTOLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUTOSERVICE)

DESCRIPTOR.services_by_name['ProdutoService'] = _PRODUTOSERVICE


_PEDIDOSERVICE = _descriptor.ServiceDescriptor(
  name='PedidoService',
  full_name='PedidoService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=257,
  serialized_end=313,
  methods=[
  _descriptor.MethodDescriptor(
    name='Pedido',
    full_name='PedidoService.Pedido',
    index=0,
    containing_service=None,
    input_type=_PRODUTOLIST,
    output_type=_PEDIDORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PEDIDOSERVICE)

DESCRIPTOR.services_by_name['PedidoService'] = _PEDIDOSERVICE

# @@protoc_insertion_point(module_scope)
