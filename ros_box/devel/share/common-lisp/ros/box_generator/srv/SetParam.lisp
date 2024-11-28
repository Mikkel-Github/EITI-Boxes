; Auto-generated. Do not edit!


(cl:in-package box_generator-srv)


;//! \htmlinclude SetParam-request.msg.html

(cl:defclass <SetParam-request> (roslisp-msg-protocol:ros-message)
  ((max_speed_xy
    :reader max_speed_xy
    :initarg :max_speed_xy
    :type cl:float
    :initform 0.0)
   (max_vel_x
    :reader max_vel_x
    :initarg :max_vel_x
    :type cl:float
    :initform 0.0)
   (acc_lim_x
    :reader acc_lim_x
    :initarg :acc_lim_x
    :type cl:float
    :initform 0.0)
   (decel_lim_x
    :reader decel_lim_x
    :initarg :decel_lim_x
    :type cl:float
    :initform 0.0)
   (max_vel_theta
    :reader max_vel_theta
    :initarg :max_vel_theta
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetParam-request (<SetParam-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetParam-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetParam-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name box_generator-srv:<SetParam-request> is deprecated: use box_generator-srv:SetParam-request instead.")))

(cl:ensure-generic-function 'max_speed_xy-val :lambda-list '(m))
(cl:defmethod max_speed_xy-val ((m <SetParam-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:max_speed_xy-val is deprecated.  Use box_generator-srv:max_speed_xy instead.")
  (max_speed_xy m))

(cl:ensure-generic-function 'max_vel_x-val :lambda-list '(m))
(cl:defmethod max_vel_x-val ((m <SetParam-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:max_vel_x-val is deprecated.  Use box_generator-srv:max_vel_x instead.")
  (max_vel_x m))

(cl:ensure-generic-function 'acc_lim_x-val :lambda-list '(m))
(cl:defmethod acc_lim_x-val ((m <SetParam-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:acc_lim_x-val is deprecated.  Use box_generator-srv:acc_lim_x instead.")
  (acc_lim_x m))

(cl:ensure-generic-function 'decel_lim_x-val :lambda-list '(m))
(cl:defmethod decel_lim_x-val ((m <SetParam-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:decel_lim_x-val is deprecated.  Use box_generator-srv:decel_lim_x instead.")
  (decel_lim_x m))

(cl:ensure-generic-function 'max_vel_theta-val :lambda-list '(m))
(cl:defmethod max_vel_theta-val ((m <SetParam-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:max_vel_theta-val is deprecated.  Use box_generator-srv:max_vel_theta instead.")
  (max_vel_theta m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetParam-request>) ostream)
  "Serializes a message object of type '<SetParam-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'max_speed_xy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'max_vel_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'acc_lim_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'decel_lim_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'max_vel_theta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetParam-request>) istream)
  "Deserializes a message object of type '<SetParam-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_speed_xy) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_vel_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'acc_lim_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'decel_lim_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_vel_theta) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetParam-request>)))
  "Returns string type for a service object of type '<SetParam-request>"
  "box_generator/SetParamRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetParam-request)))
  "Returns string type for a service object of type 'SetParam-request"
  "box_generator/SetParamRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetParam-request>)))
  "Returns md5sum for a message object of type '<SetParam-request>"
  "3e7c329fec6fea0b39dd75f575b3c45d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetParam-request)))
  "Returns md5sum for a message object of type 'SetParam-request"
  "3e7c329fec6fea0b39dd75f575b3c45d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetParam-request>)))
  "Returns full string definition for message of type '<SetParam-request>"
  (cl:format cl:nil "float32 max_speed_xy~%float32 max_vel_x~%float32 acc_lim_x~%float32 decel_lim_x~%float32 max_vel_theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetParam-request)))
  "Returns full string definition for message of type 'SetParam-request"
  (cl:format cl:nil "float32 max_speed_xy~%float32 max_vel_x~%float32 acc_lim_x~%float32 decel_lim_x~%float32 max_vel_theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetParam-request>))
  (cl:+ 0
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetParam-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetParam-request
    (cl:cons ':max_speed_xy (max_speed_xy msg))
    (cl:cons ':max_vel_x (max_vel_x msg))
    (cl:cons ':acc_lim_x (acc_lim_x msg))
    (cl:cons ':decel_lim_x (decel_lim_x msg))
    (cl:cons ':max_vel_theta (max_vel_theta msg))
))
;//! \htmlinclude SetParam-response.msg.html

(cl:defclass <SetParam-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (status_message
    :reader status_message
    :initarg :status_message
    :type cl:string
    :initform ""))
)

(cl:defclass SetParam-response (<SetParam-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetParam-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetParam-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name box_generator-srv:<SetParam-response> is deprecated: use box_generator-srv:SetParam-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetParam-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:success-val is deprecated.  Use box_generator-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'status_message-val :lambda-list '(m))
(cl:defmethod status_message-val ((m <SetParam-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:status_message-val is deprecated.  Use box_generator-srv:status_message instead.")
  (status_message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetParam-response>) ostream)
  "Serializes a message object of type '<SetParam-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'status_message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'status_message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetParam-response>) istream)
  "Deserializes a message object of type '<SetParam-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status_message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'status_message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetParam-response>)))
  "Returns string type for a service object of type '<SetParam-response>"
  "box_generator/SetParamResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetParam-response)))
  "Returns string type for a service object of type 'SetParam-response"
  "box_generator/SetParamResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetParam-response>)))
  "Returns md5sum for a message object of type '<SetParam-response>"
  "3e7c329fec6fea0b39dd75f575b3c45d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetParam-response)))
  "Returns md5sum for a message object of type 'SetParam-response"
  "3e7c329fec6fea0b39dd75f575b3c45d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetParam-response>)))
  "Returns full string definition for message of type '<SetParam-response>"
  (cl:format cl:nil "bool success~%string status_message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetParam-response)))
  "Returns full string definition for message of type 'SetParam-response"
  (cl:format cl:nil "bool success~%string status_message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetParam-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'status_message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetParam-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetParam-response
    (cl:cons ':success (success msg))
    (cl:cons ':status_message (status_message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetParam)))
  'SetParam-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetParam)))
  'SetParam-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetParam)))
  "Returns string type for a service object of type '<SetParam>"
  "box_generator/SetParam")