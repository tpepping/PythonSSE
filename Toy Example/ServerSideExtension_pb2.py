# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ServerSideExtension.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ServerSideExtension.proto',
  package='qlik.sse',
  syntax='proto3',
  serialized_pb=_b('\n\x19ServerSideExtension.proto\x12\x08qlik.sse\"\x07\n\x05\x45mpty\"?\n\tParameter\x12$\n\x08\x64\x61taType\x18\x01 \x01(\x0e\x32\x12.qlik.sse.DataType\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xb1\x01\n\x12\x46unctionDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x0c\x66unctionType\x18\x02 \x01(\x0e\x32\x16.qlik.sse.FunctionType\x12&\n\nreturnType\x18\x03 \x01(\x0e\x32\x12.qlik.sse.DataType\x12#\n\x06params\x18\x04 \x03(\x0b\x32\x13.qlik.sse.Parameter\x12\x12\n\nfunctionId\x18\x05 \x01(\x05\"\x85\x01\n\x0c\x43\x61pabilities\x12\x13\n\x0b\x61llowScript\x18\x01 \x01(\x08\x12/\n\tfunctions\x18\x02 \x03(\x0b\x32\x1c.qlik.sse.FunctionDefinition\x12\x18\n\x10pluginIdentifier\x18\x03 \x01(\t\x12\x15\n\rpluginVersion\x18\x04 \x01(\t\"(\n\x04\x44ual\x12\x0f\n\x07numData\x18\x01 \x01(\x01\x12\x0f\n\x07strData\x18\x02 \x01(\t\"$\n\x03Row\x12\x1d\n\x05\x64uals\x18\x01 \x03(\x0b\x32\x0e.qlik.sse.Dual\"*\n\x0b\x42undledRows\x12\x1b\n\x04rows\x18\x01 \x03(\x0b\x32\r.qlik.sse.Row\"\xa0\x01\n\x13ScriptRequestHeader\x12\x0e\n\x06script\x18\x01 \x01(\t\x12,\n\x0c\x66unctionType\x18\x02 \x01(\x0e\x32\x16.qlik.sse.FunctionType\x12&\n\nreturnType\x18\x03 \x01(\x0e\x32\x12.qlik.sse.DataType\x12#\n\x06params\x18\x04 \x03(\x0b\x32\x13.qlik.sse.Parameter\"<\n\x15\x46unctionRequestHeader\x12\x12\n\nfunctionId\x18\x01 \x01(\x05\x12\x0f\n\x07version\x18\x02 \x01(\t\"I\n\x13\x43ommonRequestHeader\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61rdinality\x18\x03 \x01(\x03*-\n\x08\x44\x61taType\x12\n\n\x06STRING\x10\x00\x12\x0b\n\x07NUMERIC\x10\x01\x12\x08\n\x04\x44UAL\x10\x02*7\n\x0c\x46unctionType\x12\n\n\x06SCALAR\x10\x00\x12\x0f\n\x0b\x41GGREGATION\x10\x01\x12\n\n\x06TENSOR\x10\x02\x32\xd6\x01\n\tConnector\x12<\n\x0fGetCapabilities\x12\x0f.qlik.sse.Empty\x1a\x16.qlik.sse.Capabilities\"\x00\x12\x45\n\x0f\x45xecuteFunction\x12\x15.qlik.sse.BundledRows\x1a\x15.qlik.sse.BundledRows\"\x00(\x01\x30\x01\x12\x44\n\x0e\x45valuateScript\x12\x15.qlik.sse.BundledRows\x1a\x15.qlik.sse.BundledRows\"\x00(\x01\x30\x01\x42\x03\xf8\x01\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='qlik.sse.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMERIC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=853,
  serialized_end=898,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_FUNCTIONTYPE = _descriptor.EnumDescriptor(
  name='FunctionType',
  full_name='qlik.sse.FunctionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCALAR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGGREGATION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TENSOR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=900,
  serialized_end=955,
)
_sym_db.RegisterEnumDescriptor(_FUNCTIONTYPE)

FunctionType = enum_type_wrapper.EnumTypeWrapper(_FUNCTIONTYPE)
STRING = 0
NUMERIC = 1
DUAL = 2
SCALAR = 0
AGGREGATION = 1
TENSOR = 2



_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='qlik.sse.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=46,
)


_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='qlik.sse.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataType', full_name='qlik.sse.Parameter.dataType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='qlik.sse.Parameter.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=111,
)


_FUNCTIONDEFINITION = _descriptor.Descriptor(
  name='FunctionDefinition',
  full_name='qlik.sse.FunctionDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='qlik.sse.FunctionDefinition.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functionType', full_name='qlik.sse.FunctionDefinition.functionType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='returnType', full_name='qlik.sse.FunctionDefinition.returnType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='qlik.sse.FunctionDefinition.params', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functionId', full_name='qlik.sse.FunctionDefinition.functionId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=291,
)


_CAPABILITIES = _descriptor.Descriptor(
  name='Capabilities',
  full_name='qlik.sse.Capabilities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowScript', full_name='qlik.sse.Capabilities.allowScript', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functions', full_name='qlik.sse.Capabilities.functions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pluginIdentifier', full_name='qlik.sse.Capabilities.pluginIdentifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pluginVersion', full_name='qlik.sse.Capabilities.pluginVersion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=427,
)


_DUAL = _descriptor.Descriptor(
  name='Dual',
  full_name='qlik.sse.Dual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numData', full_name='qlik.sse.Dual.numData', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strData', full_name='qlik.sse.Dual.strData', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=469,
)


_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='qlik.sse.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='duals', full_name='qlik.sse.Row.duals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=507,
)


_BUNDLEDROWS = _descriptor.Descriptor(
  name='BundledRows',
  full_name='qlik.sse.BundledRows',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='qlik.sse.BundledRows.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=551, 
)


_SCRIPTREQUESTHEADER = _descriptor.Descriptor(
  name='ScriptRequestHeader',
  full_name='qlik.sse.ScriptRequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='qlik.sse.ScriptRequestHeader.script', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functionType', full_name='qlik.sse.ScriptRequestHeader.functionType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='returnType', full_name='qlik.sse.ScriptRequestHeader.returnType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='qlik.sse.ScriptRequestHeader.params', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=714,
)


_FUNCTIONREQUESTHEADER = _descriptor.Descriptor(
  name='FunctionRequestHeader',
  full_name='qlik.sse.FunctionRequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='functionId', full_name='qlik.sse.FunctionRequestHeader.functionId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='qlik.sse.FunctionRequestHeader.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=776,
)


_COMMONREQUESTHEADER = _descriptor.Descriptor(
  name='CommonRequestHeader',
  full_name='qlik.sse.CommonRequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='qlik.sse.CommonRequestHeader.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userId', full_name='qlik.sse.CommonRequestHeader.userId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cardinality', full_name='qlik.sse.CommonRequestHeader.cardinality', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=851,
)

_PARAMETER.fields_by_name['dataType'].enum_type = _DATATYPE
_FUNCTIONDEFINITION.fields_by_name['functionType'].enum_type = _FUNCTIONTYPE
_FUNCTIONDEFINITION.fields_by_name['returnType'].enum_type = _DATATYPE
_FUNCTIONDEFINITION.fields_by_name['params'].message_type = _PARAMETER
_CAPABILITIES.fields_by_name['functions'].message_type = _FUNCTIONDEFINITION
_ROW.fields_by_name['duals'].message_type = _DUAL
_BUNDLEDROWS.fields_by_name['rows'].message_type = _ROW
_SCRIPTREQUESTHEADER.fields_by_name['functionType'].enum_type = _FUNCTIONTYPE
_SCRIPTREQUESTHEADER.fields_by_name['returnType'].enum_type = _DATATYPE
_SCRIPTREQUESTHEADER.fields_by_name['params'].message_type = _PARAMETER
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['FunctionDefinition'] = _FUNCTIONDEFINITION
DESCRIPTOR.message_types_by_name['Capabilities'] = _CAPABILITIES
DESCRIPTOR.message_types_by_name['Dual'] = _DUAL
DESCRIPTOR.message_types_by_name['Row'] = _ROW
DESCRIPTOR.message_types_by_name['BundledRows'] = _BUNDLEDROWS
DESCRIPTOR.message_types_by_name['ScriptRequestHeader'] = _SCRIPTREQUESTHEADER
DESCRIPTOR.message_types_by_name['FunctionRequestHeader'] = _FUNCTIONREQUESTHEADER
DESCRIPTOR.message_types_by_name['CommonRequestHeader'] = _COMMONREQUESTHEADER
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
DESCRIPTOR.enum_types_by_name['FunctionType'] = _FUNCTIONTYPE

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.Empty)
  ))
_sym_db.RegisterMessage(Empty)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETER,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.Parameter)
  ))
_sym_db.RegisterMessage(Parameter)

FunctionDefinition = _reflection.GeneratedProtocolMessageType('FunctionDefinition', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONDEFINITION,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.FunctionDefinition)
  ))
_sym_db.RegisterMessage(FunctionDefinition)

Capabilities = _reflection.GeneratedProtocolMessageType('Capabilities', (_message.Message,), dict(
  DESCRIPTOR = _CAPABILITIES,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.Capabilities)
  ))
_sym_db.RegisterMessage(Capabilities)

Dual = _reflection.GeneratedProtocolMessageType('Dual', (_message.Message,), dict(
  DESCRIPTOR = _DUAL,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.Dual)
  ))
_sym_db.RegisterMessage(Dual)

Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
  DESCRIPTOR = _ROW,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.Row)
  ))
_sym_db.RegisterMessage(Row)

BundledRows = _reflection.GeneratedProtocolMessageType('BundledRows', (_message.Message,), dict(
  DESCRIPTOR = _BUNDLEDROWS,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.BundledRows)
  ))
_sym_db.RegisterMessage(BundledRows)

ScriptRequestHeader = _reflection.GeneratedProtocolMessageType('ScriptRequestHeader', (_message.Message,), dict(
  DESCRIPTOR = _SCRIPTREQUESTHEADER,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.ScriptRequestHeader)
  ))
_sym_db.RegisterMessage(ScriptRequestHeader)

FunctionRequestHeader = _reflection.GeneratedProtocolMessageType('FunctionRequestHeader', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONREQUESTHEADER,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.FunctionRequestHeader)
  ))
_sym_db.RegisterMessage(FunctionRequestHeader)

CommonRequestHeader = _reflection.GeneratedProtocolMessageType('CommonRequestHeader', (_message.Message,), dict(
  DESCRIPTOR = _COMMONREQUESTHEADER,
  __module__ = 'ServerSideExtension_pb2'
  # @@protoc_insertion_point(class_scope:qlik.sse.CommonRequestHeader)
  ))
_sym_db.RegisterMessage(CommonRequestHeader)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class ConnectorStub(object):
    """*
    The communication service provited between Qlik Engine and the plugin.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetCapabilities = channel.unary_unary(
          '/qlik.sse.Connector/GetCapabilities',
          request_serializer=Empty.SerializeToString,
          response_deserializer=Capabilities.FromString,
          )
      self.ExecuteFunction = channel.stream_stream(
          '/qlik.sse.Connector/ExecuteFunction',
          request_serializer=BundledRows.SerializeToString,
          response_deserializer=BundledRows.FromString,
          )
      self.EvaluateScript = channel.stream_stream(
          '/qlik.sse.Connector/EvaluateScript',
          request_serializer=BundledRows.SerializeToString,
          response_deserializer=BundledRows.FromString,
          )


  class ConnectorServicer(object):
    """*
    The communication service provited between Qlik Engine and the plugin.
    
    ## TW: If the GetCapabilities, ExecuteFunction, and EvaluateScript function are not implemented in
    ##     ExtensionService_XXX.py, then the following definitions will cause the errors to spit back
    ##     alerting the user that the uses have not been implemented.
    """

    def GetCapabilities(self, request, context):
      """/ A handshake call for the Qlik Engine to understand the capability of the plugin.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ExecuteFunction(self, request_iterator, context):
      """/ Requests a function to be executed as specified in header.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def EvaluateScript(self, request_iterator, context):
      """/ Requests a script to be evaluated as specified in header.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

  """
  ## TW: This essentially creates a dictionary of client side functions, and maps them to the
  ##     the server. So that when the GetCapabilities method on the client is sent to the 
  ##     server, it will execute the GetCapabilities method on the server. 
  """

  def add_ConnectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetCapabilities': grpc.unary_unary_rpc_method_handler( 
            servicer.GetCapabilities,
            request_deserializer=Empty.FromString,
            response_serializer=Capabilities.SerializeToString,
        ),
        'ExecuteFunction': grpc.stream_stream_rpc_method_handler(
            servicer.ExecuteFunction,
            request_deserializer=BundledRows.FromString,
            response_serializer=BundledRows.SerializeToString,
        ),
        'EvaluateScript': grpc.stream_stream_rpc_method_handler(
            servicer.EvaluateScript,
            request_deserializer=BundledRows.FromString,
            response_serializer=BundledRows.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler( ## TW: Creates a grpc.GenericHandler from RpcMethodHandlers
        'qlik.sse.Connector', rpc_method_handlers)  ## TW: 'qlik.sse.Connector' is the name of the service used for the method handlers
    server.add_generic_rpc_handlers((generic_handler,)) ## TW: This registers GenericRcpHandlers with the Server 


  class BetaConnectorServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """*
    The communication service provited between Qlik Engine and the plugin.
    """
    def GetCapabilities(self, request, context):
      """/ A handshake call for the Qlik Engine to understand the capability of the plugin.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ExecuteFunction(self, request_iterator, context):
      """/ Requests a function to be executed as specified in header.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def EvaluateScript(self, request_iterator, context):
      """/ Requests a script to be evaluated as specified in header.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaConnectorStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """*
    The communication service provited between Qlik Engine and the plugin.
    """
    def GetCapabilities(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """/ A handshake call for the Qlik Engine to understand the capability of the plugin.
      """
      raise NotImplementedError()
    GetCapabilities.future = None
    def ExecuteFunction(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      """/ Requests a function to be executed as specified in header.
      """
      raise NotImplementedError()
    def EvaluateScript(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      """/ Requests a script to be evaluated as specified in header.
      """
      raise NotImplementedError()


  def beta_create_Connector_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('qlik.sse.Connector', 'EvaluateScript'): BundledRows.FromString,
      ('qlik.sse.Connector', 'ExecuteFunction'): BundledRows.FromString,
      ('qlik.sse.Connector', 'GetCapabilities'): Empty.FromString,
    }
    response_serializers = {
      ('qlik.sse.Connector', 'EvaluateScript'): BundledRows.SerializeToString,
      ('qlik.sse.Connector', 'ExecuteFunction'): BundledRows.SerializeToString,
      ('qlik.sse.Connector', 'GetCapabilities'): Capabilities.SerializeToString,
    }
    method_implementations = {
      ('qlik.sse.Connector', 'EvaluateScript'): face_utilities.stream_stream_inline(servicer.EvaluateScript),
      ('qlik.sse.Connector', 'ExecuteFunction'): face_utilities.stream_stream_inline(servicer.ExecuteFunction),
      ('qlik.sse.Connector', 'GetCapabilities'): face_utilities.unary_unary_inline(servicer.GetCapabilities),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Connector_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('qlik.sse.Connector', 'EvaluateScript'): BundledRows.SerializeToString,
      ('qlik.sse.Connector', 'ExecuteFunction'): BundledRows.SerializeToString,
      ('qlik.sse.Connector', 'GetCapabilities'): Empty.SerializeToString,
    }
    response_deserializers = {
      ('qlik.sse.Connector', 'EvaluateScript'): BundledRows.FromString,
      ('qlik.sse.Connector', 'ExecuteFunction'): BundledRows.FromString,
      ('qlik.sse.Connector', 'GetCapabilities'): Capabilities.FromString,
    }
    cardinalities = {
      'EvaluateScript': cardinality.Cardinality.STREAM_STREAM,
      'ExecuteFunction': cardinality.Cardinality.STREAM_STREAM,
      'GetCapabilities': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'qlik.sse.Connector', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)