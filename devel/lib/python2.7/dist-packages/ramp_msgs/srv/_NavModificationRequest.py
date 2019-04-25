# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ramp_msgs/NavModificationRequestRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import nav_msgs.msg
import std_msgs.msg

class NavModificationRequestRequest(genpy.Message):
  _md5sum = "c6b0c9277cbfc20c7bb397f2349b399a"
  _type = "ramp_msgs/NavModificationRequestRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """nav_msgs/Path[] paths
string op
float64 repair_dist
float64 repair_dir
float64 repair_ob_r


================================================================================
MSG: nav_msgs/Path
#An array of poses that represents a Path for a robot to follow
Header header
geometry_msgs/PoseStamped[] poses

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['paths','op','repair_dist','repair_dir','repair_ob_r']
  _slot_types = ['nav_msgs/Path[]','string','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       paths,op,repair_dist,repair_dir,repair_ob_r

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(NavModificationRequestRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.paths is None:
        self.paths = []
      if self.op is None:
        self.op = ''
      if self.repair_dist is None:
        self.repair_dist = 0.
      if self.repair_dir is None:
        self.repair_dir = 0.
      if self.repair_ob_r is None:
        self.repair_ob_r = 0.
    else:
      self.paths = []
      self.op = ''
      self.repair_dist = 0.
      self.repair_dir = 0.
      self.repair_ob_r = 0.

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
      length = len(self.paths)
      buff.write(_struct_I.pack(length))
      for val1 in self.paths:
        _v1 = val1.header
        buff.write(_get_struct_I().pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.poses:
          _v3 = val2.header
          buff.write(_get_struct_I().pack(_v3.seq))
          _v4 = _v3.stamp
          _x = _v4
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
          _x = _v3.frame_id
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _v5 = val2.pose
          _v6 = _v5.position
          _x = _v6
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v7 = _v5.orientation
          _x = _v7
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self.op
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.repair_dist, _x.repair_dir, _x.repair_ob_r))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.paths is None:
        self.paths = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.paths = []
      for i in range(0, length):
        val1 = nav_msgs.msg.Path()
        _v8 = val1.header
        start = end
        end += 4
        (_v8.seq,) = _get_struct_I().unpack(str[start:end])
        _v9 = _v8.stamp
        _x = _v9
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v8.frame_id = str[start:end].decode('utf-8')
        else:
          _v8.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.PoseStamped()
          _v10 = val2.header
          start = end
          end += 4
          (_v10.seq,) = _get_struct_I().unpack(str[start:end])
          _v11 = _v10.stamp
          _x = _v11
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v10.frame_id = str[start:end].decode('utf-8')
          else:
            _v10.frame_id = str[start:end]
          _v12 = val2.pose
          _v13 = _v12.position
          _x = _v13
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v14 = _v12.orientation
          _x = _v14
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          val1.poses.append(val2)
        self.paths.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.op = str[start:end].decode('utf-8')
      else:
        self.op = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.repair_dist, _x.repair_dir, _x.repair_ob_r,) = _get_struct_3d().unpack(str[start:end])
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
      length = len(self.paths)
      buff.write(_struct_I.pack(length))
      for val1 in self.paths:
        _v15 = val1.header
        buff.write(_get_struct_I().pack(_v15.seq))
        _v16 = _v15.stamp
        _x = _v16
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v15.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.poses:
          _v17 = val2.header
          buff.write(_get_struct_I().pack(_v17.seq))
          _v18 = _v17.stamp
          _x = _v18
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
          _x = _v17.frame_id
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _v19 = val2.pose
          _v20 = _v19.position
          _x = _v20
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v21 = _v19.orientation
          _x = _v21
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self.op
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.repair_dist, _x.repair_dir, _x.repair_ob_r))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.paths is None:
        self.paths = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.paths = []
      for i in range(0, length):
        val1 = nav_msgs.msg.Path()
        _v22 = val1.header
        start = end
        end += 4
        (_v22.seq,) = _get_struct_I().unpack(str[start:end])
        _v23 = _v22.stamp
        _x = _v23
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v22.frame_id = str[start:end].decode('utf-8')
        else:
          _v22.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.PoseStamped()
          _v24 = val2.header
          start = end
          end += 4
          (_v24.seq,) = _get_struct_I().unpack(str[start:end])
          _v25 = _v24.stamp
          _x = _v25
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v24.frame_id = str[start:end].decode('utf-8')
          else:
            _v24.frame_id = str[start:end]
          _v26 = val2.pose
          _v27 = _v26.position
          _x = _v27
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v28 = _v26.orientation
          _x = _v28
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          val1.poses.append(val2)
        self.paths.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.op = str[start:end].decode('utf-8')
      else:
        self.op = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.repair_dist, _x.repair_dir, _x.repair_ob_r,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ramp_msgs/NavModificationRequestResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import nav_msgs.msg
import std_msgs.msg

class NavModificationRequestResponse(genpy.Message):
  _md5sum = "b7963d166317bb98c0f8e1be75dfb843"
  _type = "ramp_msgs/NavModificationRequestResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
nav_msgs/Path[]  mod_paths


================================================================================
MSG: nav_msgs/Path
#An array of poses that represents a Path for a robot to follow
Header header
geometry_msgs/PoseStamped[] poses

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['mod_paths']
  _slot_types = ['nav_msgs/Path[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       mod_paths

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(NavModificationRequestResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.mod_paths is None:
        self.mod_paths = []
    else:
      self.mod_paths = []

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
      length = len(self.mod_paths)
      buff.write(_struct_I.pack(length))
      for val1 in self.mod_paths:
        _v29 = val1.header
        buff.write(_get_struct_I().pack(_v29.seq))
        _v30 = _v29.stamp
        _x = _v30
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v29.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.poses:
          _v31 = val2.header
          buff.write(_get_struct_I().pack(_v31.seq))
          _v32 = _v31.stamp
          _x = _v32
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
          _x = _v31.frame_id
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _v33 = val2.pose
          _v34 = _v33.position
          _x = _v34
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v35 = _v33.orientation
          _x = _v35
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.mod_paths is None:
        self.mod_paths = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mod_paths = []
      for i in range(0, length):
        val1 = nav_msgs.msg.Path()
        _v36 = val1.header
        start = end
        end += 4
        (_v36.seq,) = _get_struct_I().unpack(str[start:end])
        _v37 = _v36.stamp
        _x = _v37
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v36.frame_id = str[start:end].decode('utf-8')
        else:
          _v36.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.PoseStamped()
          _v38 = val2.header
          start = end
          end += 4
          (_v38.seq,) = _get_struct_I().unpack(str[start:end])
          _v39 = _v38.stamp
          _x = _v39
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v38.frame_id = str[start:end].decode('utf-8')
          else:
            _v38.frame_id = str[start:end]
          _v40 = val2.pose
          _v41 = _v40.position
          _x = _v41
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v42 = _v40.orientation
          _x = _v42
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          val1.poses.append(val2)
        self.mod_paths.append(val1)
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
      length = len(self.mod_paths)
      buff.write(_struct_I.pack(length))
      for val1 in self.mod_paths:
        _v43 = val1.header
        buff.write(_get_struct_I().pack(_v43.seq))
        _v44 = _v43.stamp
        _x = _v44
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v43.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.poses:
          _v45 = val2.header
          buff.write(_get_struct_I().pack(_v45.seq))
          _v46 = _v45.stamp
          _x = _v46
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
          _x = _v45.frame_id
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _v47 = val2.pose
          _v48 = _v47.position
          _x = _v48
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v49 = _v47.orientation
          _x = _v49
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.mod_paths is None:
        self.mod_paths = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mod_paths = []
      for i in range(0, length):
        val1 = nav_msgs.msg.Path()
        _v50 = val1.header
        start = end
        end += 4
        (_v50.seq,) = _get_struct_I().unpack(str[start:end])
        _v51 = _v50.stamp
        _x = _v51
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v50.frame_id = str[start:end].decode('utf-8')
        else:
          _v50.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.PoseStamped()
          _v52 = val2.header
          start = end
          end += 4
          (_v52.seq,) = _get_struct_I().unpack(str[start:end])
          _v53 = _v52.stamp
          _x = _v53
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v52.frame_id = str[start:end].decode('utf-8')
          else:
            _v52.frame_id = str[start:end]
          _v54 = val2.pose
          _v55 = _v54.position
          _x = _v55
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v56 = _v54.orientation
          _x = _v56
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          val1.poses.append(val2)
        self.mod_paths.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
class NavModificationRequest(object):
  _type          = 'ramp_msgs/NavModificationRequest'
  _md5sum = '3811dc7a15f462d593d653ffa9b613c5'
  _request_class  = NavModificationRequestRequest
  _response_class = NavModificationRequestResponse