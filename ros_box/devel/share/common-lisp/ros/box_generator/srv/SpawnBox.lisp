; Auto-generated. Do not edit!


(cl:in-package box_generator-srv)


;//! \htmlinclude SpawnBox-request.msg.html

(cl:defclass <SpawnBox-request> (roslisp-msg-protocol:ros-message)
  ((boxes_id
    :reader boxes_id
    :initarg :boxes_id
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (mass
    :reader mass
    :initarg :mass
    :type cl:float
    :initform 0.0)
   (length
    :reader length
    :initarg :length
    :type cl:float
    :initform 0.0)
   (width
    :reader width
    :initarg :width
    :type cl:float
    :initform 0.0)
   (height
    :reader height
    :initarg :height
    :type cl:float
    :initform 0.0))
)

(cl:defclass SpawnBox-request (<SpawnBox-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SpawnBox-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SpawnBox-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name box_generator-srv:<SpawnBox-request> is deprecated: use box_generator-srv:SpawnBox-request instead.")))

(cl:ensure-generic-function 'boxes_id-val :lambda-list '(m))
(cl:defmethod boxes_id-val ((m <SpawnBox-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:boxes_id-val is deprecated.  Use box_generator-srv:boxes_id instead.")
  (boxes_id m))

(cl:ensure-generic-function 'mass-val :lambda-list '(m))
(cl:defmethod mass-val ((m <SpawnBox-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:mass-val is deprecated.  Use box_generator-srv:mass instead.")
  (mass m))

(cl:ensure-generic-function 'length-val :lambda-list '(m))
(cl:defmethod length-val ((m <SpawnBox-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:length-val is deprecated.  Use box_generator-srv:length instead.")
  (length m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <SpawnBox-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:width-val is deprecated.  Use box_generator-srv:width instead.")
  (width m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <SpawnBox-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:height-val is deprecated.  Use box_generator-srv:height instead.")
  (height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SpawnBox-request>) ostream)
  "Serializes a message object of type '<SpawnBox-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'boxes_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'boxes_id))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'mass))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'length))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'width))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SpawnBox-request>) istream)
  "Deserializes a message object of type '<SpawnBox-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'boxes_id) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'boxes_id)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
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
    (cl:setf (cl:slot-value msg 'length) (roslisp-utils:decode-single-float-bits bits)))
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
    (cl:setf (cl:slot-value msg 'height) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SpawnBox-request>)))
  "Returns string type for a service object of type '<SpawnBox-request>"
  "box_generator/SpawnBoxRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SpawnBox-request)))
  "Returns string type for a service object of type 'SpawnBox-request"
  "box_generator/SpawnBoxRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SpawnBox-request>)))
  "Returns md5sum for a message object of type '<SpawnBox-request>"
  "45a1e59f6217c34ce24acbd9cc8ec4e3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SpawnBox-request)))
  "Returns md5sum for a message object of type 'SpawnBox-request"
  "45a1e59f6217c34ce24acbd9cc8ec4e3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SpawnBox-request>)))
  "Returns full string definition for message of type '<SpawnBox-request>"
  (cl:format cl:nil "string[] boxes_id~%float32 mass~%float32 length~%float32 width~%float32 height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SpawnBox-request)))
  "Returns full string definition for message of type 'SpawnBox-request"
  (cl:format cl:nil "string[] boxes_id~%float32 mass~%float32 length~%float32 width~%float32 height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SpawnBox-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'boxes_id) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SpawnBox-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SpawnBox-request
    (cl:cons ':boxes_id (boxes_id msg))
    (cl:cons ':mass (mass msg))
    (cl:cons ':length (length msg))
    (cl:cons ':width (width msg))
    (cl:cons ':height (height msg))
))
;//! \htmlinclude SpawnBox-response.msg.html

(cl:defclass <SpawnBox-response> (roslisp-msg-protocol:ros-message)
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

(cl:defclass SpawnBox-response (<SpawnBox-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SpawnBox-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SpawnBox-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name box_generator-srv:<SpawnBox-response> is deprecated: use box_generator-srv:SpawnBox-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SpawnBox-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:success-val is deprecated.  Use box_generator-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'status_message-val :lambda-list '(m))
(cl:defmethod status_message-val ((m <SpawnBox-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:status_message-val is deprecated.  Use box_generator-srv:status_message instead.")
  (status_message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SpawnBox-response>) ostream)
  "Serializes a message object of type '<SpawnBox-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'status_message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'status_message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SpawnBox-response>) istream)
  "Deserializes a message object of type '<SpawnBox-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SpawnBox-response>)))
  "Returns string type for a service object of type '<SpawnBox-response>"
  "box_generator/SpawnBoxResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SpawnBox-response)))
  "Returns string type for a service object of type 'SpawnBox-response"
  "box_generator/SpawnBoxResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SpawnBox-response>)))
  "Returns md5sum for a message object of type '<SpawnBox-response>"
  "45a1e59f6217c34ce24acbd9cc8ec4e3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SpawnBox-response)))
  "Returns md5sum for a message object of type 'SpawnBox-response"
  "45a1e59f6217c34ce24acbd9cc8ec4e3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SpawnBox-response>)))
  "Returns full string definition for message of type '<SpawnBox-response>"
  (cl:format cl:nil "bool success~%string status_message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SpawnBox-response)))
  "Returns full string definition for message of type 'SpawnBox-response"
  (cl:format cl:nil "bool success~%string status_message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SpawnBox-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'status_message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SpawnBox-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SpawnBox-response
    (cl:cons ':success (success msg))
    (cl:cons ':status_message (status_message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SpawnBox)))
  'SpawnBox-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SpawnBox)))
  'SpawnBox-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SpawnBox)))
  "Returns string type for a service object of type '<SpawnBox>"
  "box_generator/SpawnBox")