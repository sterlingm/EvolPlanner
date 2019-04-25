// Auto-generated. Do not edit!

// (in-package ramp_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let nav_msgs = _finder('nav_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class NavModificationRequestRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.paths = null;
      this.op = null;
      this.repair_dist = null;
      this.repair_dir = null;
      this.repair_ob_r = null;
    }
    else {
      if (initObj.hasOwnProperty('paths')) {
        this.paths = initObj.paths
      }
      else {
        this.paths = [];
      }
      if (initObj.hasOwnProperty('op')) {
        this.op = initObj.op
      }
      else {
        this.op = '';
      }
      if (initObj.hasOwnProperty('repair_dist')) {
        this.repair_dist = initObj.repair_dist
      }
      else {
        this.repair_dist = 0.0;
      }
      if (initObj.hasOwnProperty('repair_dir')) {
        this.repair_dir = initObj.repair_dir
      }
      else {
        this.repair_dir = 0.0;
      }
      if (initObj.hasOwnProperty('repair_ob_r')) {
        this.repair_ob_r = initObj.repair_ob_r
      }
      else {
        this.repair_ob_r = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type NavModificationRequestRequest
    // Serialize message field [paths]
    // Serialize the length for message field [paths]
    bufferOffset = _serializer.uint32(obj.paths.length, buffer, bufferOffset);
    obj.paths.forEach((val) => {
      bufferOffset = nav_msgs.msg.Path.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [op]
    bufferOffset = _serializer.string(obj.op, buffer, bufferOffset);
    // Serialize message field [repair_dist]
    bufferOffset = _serializer.float64(obj.repair_dist, buffer, bufferOffset);
    // Serialize message field [repair_dir]
    bufferOffset = _serializer.float64(obj.repair_dir, buffer, bufferOffset);
    // Serialize message field [repair_ob_r]
    bufferOffset = _serializer.float64(obj.repair_ob_r, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type NavModificationRequestRequest
    let len;
    let data = new NavModificationRequestRequest(null);
    // Deserialize message field [paths]
    // Deserialize array length for message field [paths]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.paths = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.paths[i] = nav_msgs.msg.Path.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [op]
    data.op = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [repair_dist]
    data.repair_dist = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [repair_dir]
    data.repair_dir = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [repair_ob_r]
    data.repair_ob_r = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.paths.forEach((val) => {
      length += nav_msgs.msg.Path.getMessageSize(val);
    });
    length += object.op.length;
    return length + 32;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ramp_msgs/NavModificationRequestRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c6b0c9277cbfc20c7bb397f2349b399a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    nav_msgs/Path[] paths
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new NavModificationRequestRequest(null);
    if (msg.paths !== undefined) {
      resolved.paths = new Array(msg.paths.length);
      for (let i = 0; i < resolved.paths.length; ++i) {
        resolved.paths[i] = nav_msgs.msg.Path.Resolve(msg.paths[i]);
      }
    }
    else {
      resolved.paths = []
    }

    if (msg.op !== undefined) {
      resolved.op = msg.op;
    }
    else {
      resolved.op = ''
    }

    if (msg.repair_dist !== undefined) {
      resolved.repair_dist = msg.repair_dist;
    }
    else {
      resolved.repair_dist = 0.0
    }

    if (msg.repair_dir !== undefined) {
      resolved.repair_dir = msg.repair_dir;
    }
    else {
      resolved.repair_dir = 0.0
    }

    if (msg.repair_ob_r !== undefined) {
      resolved.repair_ob_r = msg.repair_ob_r;
    }
    else {
      resolved.repair_ob_r = 0.0
    }

    return resolved;
    }
};

class NavModificationRequestResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.mod_paths = null;
    }
    else {
      if (initObj.hasOwnProperty('mod_paths')) {
        this.mod_paths = initObj.mod_paths
      }
      else {
        this.mod_paths = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type NavModificationRequestResponse
    // Serialize message field [mod_paths]
    // Serialize the length for message field [mod_paths]
    bufferOffset = _serializer.uint32(obj.mod_paths.length, buffer, bufferOffset);
    obj.mod_paths.forEach((val) => {
      bufferOffset = nav_msgs.msg.Path.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type NavModificationRequestResponse
    let len;
    let data = new NavModificationRequestResponse(null);
    // Deserialize message field [mod_paths]
    // Deserialize array length for message field [mod_paths]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.mod_paths = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.mod_paths[i] = nav_msgs.msg.Path.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.mod_paths.forEach((val) => {
      length += nav_msgs.msg.Path.getMessageSize(val);
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ramp_msgs/NavModificationRequestResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b7963d166317bb98c0f8e1be75dfb843';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new NavModificationRequestResponse(null);
    if (msg.mod_paths !== undefined) {
      resolved.mod_paths = new Array(msg.mod_paths.length);
      for (let i = 0; i < resolved.mod_paths.length; ++i) {
        resolved.mod_paths[i] = nav_msgs.msg.Path.Resolve(msg.mod_paths[i]);
      }
    }
    else {
      resolved.mod_paths = []
    }

    return resolved;
    }
};

module.exports = {
  Request: NavModificationRequestRequest,
  Response: NavModificationRequestResponse,
  md5sum() { return '3811dc7a15f462d593d653ffa9b613c5'; },
  datatype() { return 'ramp_msgs/NavModificationRequest'; }
};
