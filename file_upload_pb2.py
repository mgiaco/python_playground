# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_upload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='file_upload.proto',
  package='fileupload',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x66ile_upload.proto\x12\nfileupload\"\x1a\n\nDataChunks\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x1e\n\x0cUploadStatus\x12\x0e\n\x06status\x18\x01 \x01(\t2H\n\x06Upload\x12>\n\x06Upload\x12\x16.fileupload.DataChunks\x1a\x18.fileupload.UploadStatus\"\x00(\x01\x62\x06proto3')
)




_DATACHUNKS = _descriptor.Descriptor(
  name='DataChunks',
  full_name='fileupload.DataChunks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='fileupload.DataChunks.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=33,
  serialized_end=59,
)


_UPLOADSTATUS = _descriptor.Descriptor(
  name='UploadStatus',
  full_name='fileupload.UploadStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fileupload.UploadStatus.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=61,
  serialized_end=91,
)

DESCRIPTOR.message_types_by_name['DataChunks'] = _DATACHUNKS
DESCRIPTOR.message_types_by_name['UploadStatus'] = _UPLOADSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataChunks = _reflection.GeneratedProtocolMessageType('DataChunks', (_message.Message,), dict(
  DESCRIPTOR = _DATACHUNKS,
  __module__ = 'file_upload_pb2'
  # @@protoc_insertion_point(class_scope:fileupload.DataChunks)
  ))
_sym_db.RegisterMessage(DataChunks)

UploadStatus = _reflection.GeneratedProtocolMessageType('UploadStatus', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADSTATUS,
  __module__ = 'file_upload_pb2'
  # @@protoc_insertion_point(class_scope:fileupload.UploadStatus)
  ))
_sym_db.RegisterMessage(UploadStatus)



_UPLOAD = _descriptor.ServiceDescriptor(
  name='Upload',
  full_name='fileupload.Upload',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=93,
  serialized_end=165,
  methods=[
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='fileupload.Upload.Upload',
    index=0,
    containing_service=None,
    input_type=_DATACHUNKS,
    output_type=_UPLOADSTATUS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UPLOAD)

DESCRIPTOR.services_by_name['Upload'] = _UPLOAD

# @@protoc_insertion_point(module_scope)
