# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from iiwa_msgs/CollectPoseRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CollectPoseRequest(genpy.Message):
  _md5sum = "703f20323013a67a9ef8aed4c09680ee"
  _type = "iiwa_msgs/CollectPoseRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int16 flag
"""
  __slots__ = ['flag']
  _slot_types = ['int16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       flag

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CollectPoseRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.flag is None:
        self.flag = 0
    else:
      self.flag = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_h().pack(self.flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 2
      (self.flag,) = _get_struct_h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_h().pack(self.flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 2
      (self.flag,) = _get_struct_h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_h = None
def _get_struct_h():
    global _struct_h
    if _struct_h is None:
        _struct_h = struct.Struct("<h")
    return _struct_h
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from iiwa_msgs/CollectPoseResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CollectPoseResponse(genpy.Message):
  _md5sum = "c04cda0aa82523820ae4ce5601f32ae5"
  _type = "iiwa_msgs/CollectPoseResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 position_x
float32 position_y
float32 position_z
float32 orientation_w
float32 orientation_x
float32 orientation_y
float32 orientation_z

"""
  __slots__ = ['position_x','position_y','position_z','orientation_w','orientation_x','orientation_y','orientation_z']
  _slot_types = ['float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       position_x,position_y,position_z,orientation_w,orientation_x,orientation_y,orientation_z

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CollectPoseResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.position_x is None:
        self.position_x = 0.
      if self.position_y is None:
        self.position_y = 0.
      if self.position_z is None:
        self.position_z = 0.
      if self.orientation_w is None:
        self.orientation_w = 0.
      if self.orientation_x is None:
        self.orientation_x = 0.
      if self.orientation_y is None:
        self.orientation_y = 0.
      if self.orientation_z is None:
        self.orientation_z = 0.
    else:
      self.position_x = 0.
      self.position_y = 0.
      self.position_z = 0.
      self.orientation_w = 0.
      self.orientation_x = 0.
      self.orientation_y = 0.
      self.orientation_z = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_7f().pack(_x.position_x, _x.position_y, _x.position_z, _x.orientation_w, _x.orientation_x, _x.orientation_y, _x.orientation_z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 28
      (_x.position_x, _x.position_y, _x.position_z, _x.orientation_w, _x.orientation_x, _x.orientation_y, _x.orientation_z,) = _get_struct_7f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_7f().pack(_x.position_x, _x.position_y, _x.position_z, _x.orientation_w, _x.orientation_x, _x.orientation_y, _x.orientation_z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 28
      (_x.position_x, _x.position_y, _x.position_z, _x.orientation_w, _x.orientation_x, _x.orientation_y, _x.orientation_z,) = _get_struct_7f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7f = None
def _get_struct_7f():
    global _struct_7f
    if _struct_7f is None:
        _struct_7f = struct.Struct("<7f")
    return _struct_7f
class CollectPose(object):
  _type          = 'iiwa_msgs/CollectPose'
  _md5sum = 'a9485893dad130c910b7cc6b86bb0941'
  _request_class  = CollectPoseRequest
  _response_class = CollectPoseResponse
