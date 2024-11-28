; Auto-generated. Do not edit!


(cl:in-package box_generator-srv)


;//! \htmlinclude MqttListener-request.msg.html

(cl:defclass <MqttListener-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass MqttListener-request (<MqttListener-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MqttListener-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MqttListener-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name box_generator-srv:<MqttListener-request> is deprecated: use box_generator-srv:MqttListener-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MqttListener-request>) ostream)
  "Serializes a message object of type '<MqttListener-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MqttListener-request>) istream)
  "Deserializes a message object of type '<MqttListener-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MqttListener-request>)))
  "Returns string type for a service object of type '<MqttListener-request>"
  "box_generator/MqttListenerRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MqttListener-request)))
  "Returns string type for a service object of type 'MqttListener-request"
  "box_generator/MqttListenerRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MqttListener-request>)))
  "Returns md5sum for a message object of type '<MqttListener-request>"
  "eca67f62be2b35d15d597743c12e190f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MqttListener-request)))
  "Returns md5sum for a message object of type 'MqttListener-request"
  "eca67f62be2b35d15d597743c12e190f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MqttListener-request>)))
  "Returns full string definition for message of type '<MqttListener-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MqttListener-request)))
  "Returns full string definition for message of type 'MqttListener-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MqttListener-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MqttListener-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MqttListener-request
))
;//! \htmlinclude MqttListener-response.msg.html

(cl:defclass <MqttListener-response> (roslisp-msg-protocol:ros-message)
  ((n_boxes
    :reader n_boxes
    :initarg :n_boxes
    :type cl:fixnum
    :initform 0)
   (mass
    :reader mass
    :initarg :mass
    :type cl:float
    :initform 0.0)
   (height
    :reader height
    :initarg :height
    :type cl:float
    :initform 0.0)
   (width
    :reader width
    :initarg :width
    :type cl:float
    :initform 0.0)
   (length
    :reader length
    :initarg :length
    :type cl:float
    :initform 0.0)
   (success
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

(cl:defclass MqttListener-response (<MqttListener-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MqttListener-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MqttListener-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name box_generator-srv:<MqttListener-response> is deprecated: use box_generator-srv:MqttListener-response instead.")))

(cl:ensure-generic-function 'n_boxes-val :lambda-list '(m))
(cl:defmethod n_boxes-val ((m <MqttListener-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:n_boxes-val is deprecated.  Use box_generator-srv:n_boxes instead.")
  (n_boxes m))

(cl:ensure-generic-function 'mass-val :lambda-list '(m))
(cl:defmethod mass-val ((m <MqttListener-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:mass-val is deprecated.  Use box_generator-srv:mass instead.")
  (mass m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <MqttListener-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:height-val is deprecated.  Use box_generator-srv:height instead.")
  (height m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <MqttListener-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:width-val is deprecated.  Use box_generator-srv:width instead.")
  (width m))

(cl:ensure-generic-function 'length-val :lambda-list '(m))
(cl:defmethod length-val ((m <MqttListener-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:length-val is deprecated.  Use box_generator-srv:length instead.")
  (length m))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <MqttListener-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:success-val is deprecated.  Use box_generator-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'status_message-val :lambda-list '(m))
(cl:defmethod status_message-val ((m <MqttListener-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:status_message-val is deprecated.  Use box_generator-srv:status_message instead.")
  (status_message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MqttListener-response>) ostream)
  "Serializes a message object of type '<MqttListener-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'n_boxes)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'mass))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'width))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'length))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'status_message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'status_message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MqttListener-response>) istream)
  "Deserializes a message object of type '<MqttListener-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'n_boxes)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'mass) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'height) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'width) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'length) (roslisp-utils:decode-single-float-bits bits)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MqttListener-response>)))
  "Returns string type for a service object of type '<MqttListener-response>"
  "box_generator/MqttListenerResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MqttListener-response)))
  "Returns string type for a service object of type 'MqttListener-response"
  "box_generator/MqttListenerResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MqttListener-response>)))
  "Returns md5sum for a message object of type '<MqttListener-response>"
  "eca67f62be2b35d15d597743c12e190f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MqttListener-response)))
  "Returns md5sum for a message object of type 'MqttListener-response"
  "eca67f62be2b35d15d597743c12e190f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MqttListener-response>)))
  "Returns full string definition for message of type '<MqttListener-response>"
  (cl:format cl:nil "uint8 n_boxes~%float32 mass~%float32 height~%float32 width~%float32 length~%bool success~%string status_message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MqttListener-response)))
  "Returns full string definition for message of type 'MqttListener-response"
  (cl:format cl:nil "uint8 n_boxes~%float32 mass~%float32 height~%float32 width~%float32 length~%bool success~%string status_message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MqttListener-response>))
  (cl:+ 0
     1
     4
     4
     4
     4
     1
     4 (cl:length (cl:slot-value msg 'status_message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MqttListener-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MqttListener-response
    (cl:cons ':n_boxes (n_boxes msg))
    (cl:cons ':mass (mass msg))
    (cl:cons ':height (height msg))
    (cl:cons ':width (width msg))
    (cl:cons ':length (length msg))
    (cl:cons ':success (success msg))
    (cl:cons ':status_message (status_message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MqttListener)))
  'MqttListener-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MqttListener)))
  'MqttListener-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MqttListener)))
  "Returns string type for a service object of type '<MqttListener>"
  "box_generator/MqttListener")