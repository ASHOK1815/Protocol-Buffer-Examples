# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
  name='users.proto',
  package='test_proto',
  syntax='proto3',
  serialized_options=b'\n\033com.example.tutorial.protosB\nUserProtosP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0busers.proto\x12\ntest_proto\"I\n\x04User\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x15\n\rcontactNumber\x18\x04 \x01(\x03\"(\n\x05Users\x12\x1f\n\x05users\x18\x01 \x03(\x0b\x32\x10.test_proto.UserB+\n\x1b\x63om.example.tutorial.protosB\nUserProtosP\x01\x62\x06proto3'
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='test_proto.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='test_proto.User.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='test_proto.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='test_proto.User.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contactNumber', full_name='test_proto.User.contactNumber', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=27,
  serialized_end=100,
)


_USERS = _descriptor.Descriptor(
  name='Users',
  full_name='test_proto.Users',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='test_proto.Users.users', index=0,
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
  serialized_start=102,
  serialized_end=142,
)

_USERS.fields_by_name['users'].message_type = _USER
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Users'] = _USERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:test_proto.User)
  })
_sym_db.RegisterMessage(User)

Users = _reflection.GeneratedProtocolMessageType('Users', (_message.Message,), {
  'DESCRIPTOR' : _USERS,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:test_proto.Users)
  })
_sym_db.RegisterMessage(Users)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
