# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xbuf/primitives.proto

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
  name='xbuf/primitives.proto',
  package='xbuf',
  syntax='proto3',
  serialized_pb=_b('\n\x15xbuf/primitives.proto\x12\x04xbuf\"\x1c\n\x04Vec2\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\'\n\x04Vec3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"2\n\x04Vec4\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"3\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x01(\x02\x12\t\n\x01g\x18\x02 \x01(\x02\x12\t\n\x01\x62\x18\x03 \x01(\x02\x12\t\n\x01\x61\x18\x04 \x01(\x02\"d\n\x07Texture\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x05rpath\x18\x03 \x01(\tH\x00\x12&\n\x05tex2d\x18\x04 \x01(\x0b\x32\x15.xbuf.Texture2DInlineH\x00\x42\x06\n\x04\x64\x61ta\"\xa1\x01\n\x0fTexture2DInline\x12,\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x1c.xbuf.Texture2DInline.Format\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"3\n\x06\x46ormat\x12\t\n\x05undef\x10\x00\x12\x08\n\x04rgb8\x10\x01\x12\t\n\x05rgba8\x10\x02\x12\t\n\x05\x62gra8\x10\x03\"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"\xd6\x01\n\x04Mat4\x12\x0b\n\x03\x63\x30\x30\x18\x01 \x01(\x02\x12\x0b\n\x03\x63\x31\x30\x18\x02 \x01(\x02\x12\x0b\n\x03\x63\x32\x30\x18\x03 \x01(\x02\x12\x0b\n\x03\x63\x33\x30\x18\x04 \x01(\x02\x12\x0b\n\x03\x63\x30\x31\x18\x05 \x01(\x02\x12\x0b\n\x03\x63\x31\x31\x18\x06 \x01(\x02\x12\x0b\n\x03\x63\x32\x31\x18\x07 \x01(\x02\x12\x0b\n\x03\x63\x33\x31\x18\x08 \x01(\x02\x12\x0b\n\x03\x63\x30\x32\x18\t \x01(\x02\x12\x0b\n\x03\x63\x31\x32\x18\n \x01(\x02\x12\x0b\n\x03\x63\x32\x32\x18\x0b \x01(\x02\x12\x0b\n\x03\x63\x33\x32\x18\x0c \x01(\x02\x12\x0b\n\x03\x63\x30\x33\x18\r \x01(\x02\x12\x0b\n\x03\x63\x31\x33\x18\x0e \x01(\x02\x12\x0b\n\x03\x63\x32\x33\x18\x0f \x01(\x02\x12\x0b\n\x03\x63\x33\x33\x18\x10 \x01(\x02\"k\n\tTransform\x12\x1f\n\x0btranslation\x18\x01 \x01(\x0b\x32\n.xbuf.Vec3\x12\"\n\x08rotation\x18\x02 \x01(\x0b\x32\x10.xbuf.Quaternion\x12\x19\n\x05scale\x18\x03 \x01(\x0b\x32\n.xbuf.Vec3b\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TEXTURE2DINLINE_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='xbuf.Texture2DInline.Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='undef', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='rgb8', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='rgba8', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='bgra8', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=420,
  serialized_end=471,
)
_sym_db.RegisterEnumDescriptor(_TEXTURE2DINLINE_FORMAT)


_VEC2 = _descriptor.Descriptor(
  name='Vec2',
  full_name='xbuf.Vec2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='xbuf.Vec2.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='xbuf.Vec2.y', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=59,
)


_VEC3 = _descriptor.Descriptor(
  name='Vec3',
  full_name='xbuf.Vec3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='xbuf.Vec3.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='xbuf.Vec3.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='xbuf.Vec3.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=100,
)


_VEC4 = _descriptor.Descriptor(
  name='Vec4',
  full_name='xbuf.Vec4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='xbuf.Vec4.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='xbuf.Vec4.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='xbuf.Vec4.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='xbuf.Vec4.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=152,
)


_COLOR = _descriptor.Descriptor(
  name='Color',
  full_name='xbuf.Color',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r', full_name='xbuf.Color.r', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='g', full_name='xbuf.Color.g', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='xbuf.Color.b', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a', full_name='xbuf.Color.a', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=205,
)


_TEXTURE = _descriptor.Descriptor(
  name='Texture',
  full_name='xbuf.Texture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xbuf.Texture.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='xbuf.Texture.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpath', full_name='xbuf.Texture.rpath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tex2d', full_name='xbuf.Texture.tex2d', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='xbuf.Texture.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=207,
  serialized_end=307,
)


_TEXTURE2DINLINE = _descriptor.Descriptor(
  name='Texture2DInline',
  full_name='xbuf.Texture2DInline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='xbuf.Texture2DInline.format', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='xbuf.Texture2DInline.width', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='xbuf.Texture2DInline.height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='xbuf.Texture2DInline.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TEXTURE2DINLINE_FORMAT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=471,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='xbuf.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='xbuf.Quaternion.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='xbuf.Quaternion.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='xbuf.Quaternion.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='xbuf.Quaternion.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=529,
)


_MAT4 = _descriptor.Descriptor(
  name='Mat4',
  full_name='xbuf.Mat4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c00', full_name='xbuf.Mat4.c00', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c10', full_name='xbuf.Mat4.c10', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c20', full_name='xbuf.Mat4.c20', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c30', full_name='xbuf.Mat4.c30', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c01', full_name='xbuf.Mat4.c01', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c11', full_name='xbuf.Mat4.c11', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c21', full_name='xbuf.Mat4.c21', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c31', full_name='xbuf.Mat4.c31', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c02', full_name='xbuf.Mat4.c02', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c12', full_name='xbuf.Mat4.c12', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c22', full_name='xbuf.Mat4.c22', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c32', full_name='xbuf.Mat4.c32', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c03', full_name='xbuf.Mat4.c03', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c13', full_name='xbuf.Mat4.c13', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c23', full_name='xbuf.Mat4.c23', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c33', full_name='xbuf.Mat4.c33', index=15,
      number=16, type=2, cpp_type=6, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=746,
)


_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='xbuf.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='xbuf.Transform.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='xbuf.Transform.rotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='xbuf.Transform.scale', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=748,
  serialized_end=855,
)

_TEXTURE.fields_by_name['tex2d'].message_type = _TEXTURE2DINLINE
_TEXTURE.oneofs_by_name['data'].fields.append(
  _TEXTURE.fields_by_name['rpath'])
_TEXTURE.fields_by_name['rpath'].containing_oneof = _TEXTURE.oneofs_by_name['data']
_TEXTURE.oneofs_by_name['data'].fields.append(
  _TEXTURE.fields_by_name['tex2d'])
_TEXTURE.fields_by_name['tex2d'].containing_oneof = _TEXTURE.oneofs_by_name['data']
_TEXTURE2DINLINE.fields_by_name['format'].enum_type = _TEXTURE2DINLINE_FORMAT
_TEXTURE2DINLINE_FORMAT.containing_type = _TEXTURE2DINLINE
_TRANSFORM.fields_by_name['translation'].message_type = _VEC3
_TRANSFORM.fields_by_name['rotation'].message_type = _QUATERNION
_TRANSFORM.fields_by_name['scale'].message_type = _VEC3
DESCRIPTOR.message_types_by_name['Vec2'] = _VEC2
DESCRIPTOR.message_types_by_name['Vec3'] = _VEC3
DESCRIPTOR.message_types_by_name['Vec4'] = _VEC4
DESCRIPTOR.message_types_by_name['Color'] = _COLOR
DESCRIPTOR.message_types_by_name['Texture'] = _TEXTURE
DESCRIPTOR.message_types_by_name['Texture2DInline'] = _TEXTURE2DINLINE
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
DESCRIPTOR.message_types_by_name['Mat4'] = _MAT4
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM

Vec2 = _reflection.GeneratedProtocolMessageType('Vec2', (_message.Message,), dict(
  DESCRIPTOR = _VEC2,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Vec2)
  ))
_sym_db.RegisterMessage(Vec2)

Vec3 = _reflection.GeneratedProtocolMessageType('Vec3', (_message.Message,), dict(
  DESCRIPTOR = _VEC3,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Vec3)
  ))
_sym_db.RegisterMessage(Vec3)

Vec4 = _reflection.GeneratedProtocolMessageType('Vec4', (_message.Message,), dict(
  DESCRIPTOR = _VEC4,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Vec4)
  ))
_sym_db.RegisterMessage(Vec4)

Color = _reflection.GeneratedProtocolMessageType('Color', (_message.Message,), dict(
  DESCRIPTOR = _COLOR,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Color)
  ))
_sym_db.RegisterMessage(Color)

Texture = _reflection.GeneratedProtocolMessageType('Texture', (_message.Message,), dict(
  DESCRIPTOR = _TEXTURE,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Texture)
  ))
_sym_db.RegisterMessage(Texture)

Texture2DInline = _reflection.GeneratedProtocolMessageType('Texture2DInline', (_message.Message,), dict(
  DESCRIPTOR = _TEXTURE2DINLINE,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Texture2DInline)
  ))
_sym_db.RegisterMessage(Texture2DInline)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), dict(
  DESCRIPTOR = _QUATERNION,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Quaternion)
  ))
_sym_db.RegisterMessage(Quaternion)

Mat4 = _reflection.GeneratedProtocolMessageType('Mat4', (_message.Message,), dict(
  DESCRIPTOR = _MAT4,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Mat4)
  ))
_sym_db.RegisterMessage(Mat4)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORM,
  __module__ = 'xbuf.primitives_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Transform)
  ))
_sym_db.RegisterMessage(Transform)


# @@protoc_insertion_point(module_scope)
