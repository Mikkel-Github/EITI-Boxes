// Auto-generated. Do not edit!

// (in-package box_generator.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetParamRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.max_speed_xy = null;
      this.max_vel_x = null;
      this.acc_lim_x = null;
      this.decel_lim_x = null;
      this.max_vel_theta = null;
    }
    else {
      if (initObj.hasOwnProperty('max_speed_xy')) {
        this.max_speed_xy = initObj.max_speed_xy
      }
      else {
        this.max_speed_xy = 0.0;
      }
      if (initObj.hasOwnProperty('max_vel_x')) {
        this.max_vel_x = initObj.max_vel_x
      }
      else {
        this.max_vel_x = 0.0;
      }
      if (initObj.hasOwnProperty('acc_lim_x')) {
        this.acc_lim_x = initObj.acc_lim_x
      }
      else {
        this.acc_lim_x = 0.0;
      }
      if (initObj.hasOwnProperty('decel_lim_x')) {
        this.decel_lim_x = initObj.decel_lim_x
      }
      else {
        this.decel_lim_x = 0.0;
      }
      if (initObj.hasOwnProperty('max_vel_theta')) {
        this.max_vel_theta = initObj.max_vel_theta
      }
      else {
        this.max_vel_theta = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetParamRequest
    // Serialize message field [max_speed_xy]
    bufferOffset = _serializer.float32(obj.max_speed_xy, buffer, bufferOffset);
    // Serialize message field [max_vel_x]
    bufferOffset = _serializer.float32(obj.max_vel_x, buffer, bufferOffset);
    // Serialize message field [acc_lim_x]
    bufferOffset = _serializer.float32(obj.acc_lim_x, buffer, bufferOffset);
    // Serialize message field [decel_lim_x]
    bufferOffset = _serializer.float32(obj.decel_lim_x, buffer, bufferOffset);
    // Serialize message field [max_vel_theta]
    bufferOffset = _serializer.float32(obj.max_vel_theta, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetParamRequest
    let len;
    let data = new SetParamRequest(null);
    // Deserialize message field [max_speed_xy]
    data.max_speed_xy = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [max_vel_x]
    data.max_vel_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [acc_lim_x]
    data.acc_lim_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [decel_lim_x]
    data.decel_lim_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [max_vel_theta]
    data.max_vel_theta = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 20;
  }

  static datatype() {
    // Returns string type for a service object
    return 'box_generator/SetParamRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c9469833eb98d5e9c2982ce6ee19b2e3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 max_speed_xy
    float32 max_vel_x
    float32 acc_lim_x
    float32 decel_lim_x
    float32 max_vel_theta
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetParamRequest(null);
    if (msg.max_speed_xy !== undefined) {
      resolved.max_speed_xy = msg.max_speed_xy;
    }
    else {
      resolved.max_speed_xy = 0.0
    }

    if (msg.max_vel_x !== undefined) {
      resolved.max_vel_x = msg.max_vel_x;
    }
    else {
      resolved.max_vel_x = 0.0
    }

    if (msg.acc_lim_x !== undefined) {
      resolved.acc_lim_x = msg.acc_lim_x;
    }
    else {
      resolved.acc_lim_x = 0.0
    }

    if (msg.decel_lim_x !== undefined) {
      resolved.decel_lim_x = msg.decel_lim_x;
    }
    else {
      resolved.decel_lim_x = 0.0
    }

    if (msg.max_vel_theta !== undefined) {
      resolved.max_vel_theta = msg.max_vel_theta;
    }
    else {
      resolved.max_vel_theta = 0.0
    }

    return resolved;
    }
};

class SetParamResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
      this.status_message = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
      if (initObj.hasOwnProperty('status_message')) {
        this.status_message = initObj.status_message
      }
      else {
        this.status_message = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetParamResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    // Serialize message field [status_message]
    bufferOffset = _serializer.string(obj.status_message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetParamResponse
    let len;
    let data = new SetParamResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [status_message]
    data.status_message = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.status_message);
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'box_generator/SetParamResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2ec6f3eff0161f4257b808b12bc830c2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    string status_message
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetParamResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    if (msg.status_message !== undefined) {
      resolved.status_message = msg.status_message;
    }
    else {
      resolved.status_message = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: SetParamRequest,
  Response: SetParamResponse,
  md5sum() { return '3e7c329fec6fea0b39dd75f575b3c45d'; },
  datatype() { return 'box_generator/SetParam'; }
};
