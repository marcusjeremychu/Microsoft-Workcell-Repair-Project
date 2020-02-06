// Auto-generated. Do not edit!

// (in-package iiwa_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let MoveAlongSplineActionGoal = require('./MoveAlongSplineActionGoal.js');
let MoveAlongSplineActionResult = require('./MoveAlongSplineActionResult.js');
let MoveAlongSplineActionFeedback = require('./MoveAlongSplineActionFeedback.js');

//-----------------------------------------------------------

class MoveAlongSplineAction {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.action_goal = null;
      this.action_result = null;
      this.action_feedback = null;
    }
    else {
      if (initObj.hasOwnProperty('action_goal')) {
        this.action_goal = initObj.action_goal
      }
      else {
        this.action_goal = new MoveAlongSplineActionGoal();
      }
      if (initObj.hasOwnProperty('action_result')) {
        this.action_result = initObj.action_result
      }
      else {
        this.action_result = new MoveAlongSplineActionResult();
      }
      if (initObj.hasOwnProperty('action_feedback')) {
        this.action_feedback = initObj.action_feedback
      }
      else {
        this.action_feedback = new MoveAlongSplineActionFeedback();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MoveAlongSplineAction
    // Serialize message field [action_goal]
    bufferOffset = MoveAlongSplineActionGoal.serialize(obj.action_goal, buffer, bufferOffset);
    // Serialize message field [action_result]
    bufferOffset = MoveAlongSplineActionResult.serialize(obj.action_result, buffer, bufferOffset);
    // Serialize message field [action_feedback]
    bufferOffset = MoveAlongSplineActionFeedback.serialize(obj.action_feedback, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveAlongSplineAction
    let len;
    let data = new MoveAlongSplineAction(null);
    // Deserialize message field [action_goal]
    data.action_goal = MoveAlongSplineActionGoal.deserialize(buffer, bufferOffset);
    // Deserialize message field [action_result]
    data.action_result = MoveAlongSplineActionResult.deserialize(buffer, bufferOffset);
    // Deserialize message field [action_feedback]
    data.action_feedback = MoveAlongSplineActionFeedback.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += MoveAlongSplineActionGoal.getMessageSize(object.action_goal);
    length += MoveAlongSplineActionResult.getMessageSize(object.action_result);
    length += MoveAlongSplineActionFeedback.getMessageSize(object.action_feedback);
    return length;
  }

  static datatype() {
    // Returns string type for a message object
    return 'iiwa_msgs/MoveAlongSplineAction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8a9cc41458c3e11a14e647ba3c0068f7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    
    MoveAlongSplineActionGoal action_goal
    MoveAlongSplineActionResult action_result
    MoveAlongSplineActionFeedback action_feedback
    
    ================================================================================
    MSG: iiwa_msgs/MoveAlongSplineActionGoal
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    
    Header header
    actionlib_msgs/GoalID goal_id
    MoveAlongSplineGoal goal
    
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
    MSG: actionlib_msgs/GoalID
    # The stamp should store the time at which this goal was requested.
    # It is used by an action server when it tries to preempt all
    # goals that were requested before a certain time
    time stamp
    
    # The id provides a way to associate feedback and
    # result message with specific goal requests. The id
    # specified must be unique.
    string id
    
    
    ================================================================================
    MSG: iiwa_msgs/MoveAlongSplineGoal
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Goal
    Spline spline
    
    
    ================================================================================
    MSG: iiwa_msgs/Spline
    # The describes a motion along a spline
    
    SplineSegment[] segments
    ================================================================================
    MSG: iiwa_msgs/SplineSegment
    # This message describes a segment of a spline path
    
    int32 SPL = 0
    int32 LIN =  1
    int32 CIRC = 2
    
    # The type of the spline segment
    int32 type
    
    # The endpoint of the current segment
    CartesianPose point
    
    # Auxiliary point. Only used for circular segments
    CartesianPose point_aux
    ================================================================================
    MSG: iiwa_msgs/CartesianPose
    # Target Pose including redundancy information.
    geometry_msgs/PoseStamped poseStamped
    
    # If you have issues with the robot not executing the motion copy this value from the Cartesian Position Tab of the
    # robot SmartPad. Set both parameters to -1 to disable them.
    RedundancyInformation redundancy
    
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
    
    ================================================================================
    MSG: iiwa_msgs/RedundancyInformation
    # E1 parameter
    # Specifies Angle of the elbow joint.
    float64 e1
    
    # Status parameter
    #   Bit 0: 1 - The robot is working above its head
    #          0 - The robot is working in the ground area
    #   Bit 1: 1 - Angle A4 < 0°
    #          0 - Angle A4 >= 0°
    #   Bit 2: 1 - Angle A6 <= 0
    #          0 - Angle A6 > 0
    int32 status
    
    # Turn parameter
    # According to Sunrise handbook this is not used for the iiwa.
    int32 turn
    
    ================================================================================
    MSG: iiwa_msgs/MoveAlongSplineActionResult
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    
    Header header
    actionlib_msgs/GoalStatus status
    MoveAlongSplineResult result
    
    ================================================================================
    MSG: actionlib_msgs/GoalStatus
    GoalID goal_id
    uint8 status
    uint8 PENDING         = 0   # The goal has yet to be processed by the action server
    uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
    uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                                #   and has since completed its execution (Terminal State)
    uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
    uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                                #    to some failure (Terminal State)
    uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                                #    because the goal was unattainable or invalid (Terminal State)
    uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                                #    and has not yet completed execution
    uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                                #    but the action server has not yet confirmed that the goal is canceled
    uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                                #    and was successfully cancelled (Terminal State)
    uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                                #    sent over the wire by an action server
    
    #Allow for the user to associate a string with GoalStatus for debugging
    string text
    
    
    ================================================================================
    MSG: iiwa_msgs/MoveAlongSplineResult
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Result
    bool success
    string error
    
    
    ================================================================================
    MSG: iiwa_msgs/MoveAlongSplineActionFeedback
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    
    Header header
    actionlib_msgs/GoalStatus status
    MoveAlongSplineFeedback feedback
    
    ================================================================================
    MSG: iiwa_msgs/MoveAlongSplineFeedback
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Feedback
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MoveAlongSplineAction(null);
    if (msg.action_goal !== undefined) {
      resolved.action_goal = MoveAlongSplineActionGoal.Resolve(msg.action_goal)
    }
    else {
      resolved.action_goal = new MoveAlongSplineActionGoal()
    }

    if (msg.action_result !== undefined) {
      resolved.action_result = MoveAlongSplineActionResult.Resolve(msg.action_result)
    }
    else {
      resolved.action_result = new MoveAlongSplineActionResult()
    }

    if (msg.action_feedback !== undefined) {
      resolved.action_feedback = MoveAlongSplineActionFeedback.Resolve(msg.action_feedback)
    }
    else {
      resolved.action_feedback = new MoveAlongSplineActionFeedback()
    }

    return resolved;
    }
};

module.exports = MoveAlongSplineAction;
