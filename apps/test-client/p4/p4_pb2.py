# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p4.proto

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


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='p4.proto',
  package='p4',
  syntax='proto3',
  serialized_pb=_b('\n\x08p4.proto\x12\x02p4\x1a google/protobuf/descriptor.proto\"\xc1\x01\n\x06P4_int\x12\x11\n\tswitch_id\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x13\n\x0breplication\x18\x03 \x01(\x03\x12\t\n\x01\x63\x18\x04 \x01(\x03\x12\x1a\n\x12hop_count_exceeded\x18\x05 \x01(\x03\x12\x12\n\ninst_count\x18\x06 \x01(\x03\x12\x15\n\rMax_hop_count\x18\x07 \x01(\x03\x12,\n\x0fp4_int_metadata\x18\x08 \x03(\x0b\x32\x13.p4.P4_int_metadata\"\xdc\x01\n\x0fP4_int_metadata\x12\x16\n\x04type\x18\x01 \x01(\x0e\x32\x08.p4.Type\x12\x11\n\tswitch_id\x18\x02 \x01(\x03\x12\x0f\n\x07item_id\x18\x03 \x01(\x03\x12 \n\x18\x63_plane_state_ver_number\x18\x04 \x01(\x03\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x12+\n\x04kpis\x18\x06 \x03(\x0b\x32\x1d.p4.P4_int_metadata.KpisEntry\x1a+\n\tKpisEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01*+\n\x04Type\x12\x0b\n\x07ingress\x10\x00\x12\n\n\x06\x65gress\x10\x01\x12\n\n\x06\x62uffer\x10\x02\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='p4.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ingress', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='egress', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='buffer', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=469,
  serialized_end=512,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
ingress = 0
egress = 1
buffer = 2



_P4_INT = _descriptor.Descriptor(
  name='P4_int',
  full_name='p4.P4_int',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch_id', full_name='p4.P4_int.switch_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='p4.P4_int.version', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replication', full_name='p4.P4_int.replication', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c', full_name='p4.P4_int.c', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hop_count_exceeded', full_name='p4.P4_int.hop_count_exceeded', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inst_count', full_name='p4.P4_int.inst_count', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Max_hop_count', full_name='p4.P4_int.Max_hop_count', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p4_int_metadata', full_name='p4.P4_int.p4_int_metadata', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=51,
  serialized_end=244,
)


_P4_INT_METADATA_KPISENTRY = _descriptor.Descriptor(
  name='KpisEntry',
  full_name='p4.P4_int_metadata.KpisEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='p4.P4_int_metadata.KpisEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='p4.P4_int_metadata.KpisEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=467,
)

_P4_INT_METADATA = _descriptor.Descriptor(
  name='P4_int_metadata',
  full_name='p4.P4_int_metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='p4.P4_int_metadata.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_id', full_name='p4.P4_int_metadata.switch_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='p4.P4_int_metadata.item_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c_plane_state_ver_number', full_name='p4.P4_int_metadata.c_plane_state_ver_number', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='p4.P4_int_metadata.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kpis', full_name='p4.P4_int_metadata.kpis', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_P4_INT_METADATA_KPISENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=467,
)

_P4_INT.fields_by_name['p4_int_metadata'].message_type = _P4_INT_METADATA
_P4_INT_METADATA_KPISENTRY.containing_type = _P4_INT_METADATA
_P4_INT_METADATA.fields_by_name['type'].enum_type = _TYPE
_P4_INT_METADATA.fields_by_name['kpis'].message_type = _P4_INT_METADATA_KPISENTRY
DESCRIPTOR.message_types_by_name['P4_int'] = _P4_INT
DESCRIPTOR.message_types_by_name['P4_int_metadata'] = _P4_INT_METADATA
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

P4_int = _reflection.GeneratedProtocolMessageType('P4_int', (_message.Message,), dict(
  DESCRIPTOR = _P4_INT,
  __module__ = 'p4_pb2'
  # @@protoc_insertion_point(class_scope:p4.P4_int)
  ))
_sym_db.RegisterMessage(P4_int)

P4_int_metadata = _reflection.GeneratedProtocolMessageType('P4_int_metadata', (_message.Message,), dict(

  KpisEntry = _reflection.GeneratedProtocolMessageType('KpisEntry', (_message.Message,), dict(
    DESCRIPTOR = _P4_INT_METADATA_KPISENTRY,
    __module__ = 'p4_pb2'
    # @@protoc_insertion_point(class_scope:p4.P4_int_metadata.KpisEntry)
    ))
  ,
  DESCRIPTOR = _P4_INT_METADATA,
  __module__ = 'p4_pb2'
  # @@protoc_insertion_point(class_scope:p4.P4_int_metadata)
  ))
_sym_db.RegisterMessage(P4_int_metadata)
_sym_db.RegisterMessage(P4_int_metadata.KpisEntry)


_P4_INT_METADATA_KPISENTRY.has_options = True
_P4_INT_METADATA_KPISENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)