; Auto-generated. Do not edit!


(cl:in-package box_generator-srv)


;//! \htmlinclude DeleteBox-request.msg.html

(cl:defclass <DeleteBox-request> (roslisp-msg-protocol:ros-message)
  ((boxes_id
    :reader boxes_id
    :initarg :boxes_id
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass DeleteBox-request (<DeleteBox-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DeleteBox-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DeleteBox-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name box_generator-srv:<DeleteBox-request> is deprecated: use box_generator-srv:DeleteBox-request instead.")))

(cl:ensure-generic-function 'boxes_id-val :lambda-list '(m))
(cl:defmethod boxes_id-val ((m <DeleteBox-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:boxes_id-val is deprecated.  Use box_generator-srv:boxes_id instead.")
  (boxes_id m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DeleteBox-request>) ostream)
  "Serializes a message object of type '<DeleteBox-request>"
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
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DeleteBox-request>) istream)
  "Deserializes a message object of type '<DeleteBox-request>"
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DeleteBox-request>)))
  "Returns string type for a service object of type '<DeleteBox-request>"
  "box_generator/DeleteBoxRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DeleteBox-request)))
  "Returns string type for a service object of type 'DeleteBox-request"
  "box_generator/DeleteBoxRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DeleteBox-request>)))
  "Returns md5sum for a message object of type '<DeleteBox-request>"
  "82214afe4ff077ebd4b8aa0c572e1255")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DeleteBox-request)))
  "Returns md5sum for a message object of type 'DeleteBox-request"
  "82214afe4ff077ebd4b8aa0c572e1255")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DeleteBox-request>)))
  "Returns full string definition for message of type '<DeleteBox-request>"
  (cl:format cl:nil "string[] boxes_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DeleteBox-request)))
  "Returns full string definition for message of type 'DeleteBox-request"
  (cl:format cl:nil "string[] boxes_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DeleteBox-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'boxes_id) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DeleteBox-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DeleteBox-request
    (cl:cons ':boxes_id (boxes_id msg))
))
;//! \htmlinclude DeleteBox-response.msg.html

(cl:defclass <DeleteBox-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass DeleteBox-response (<DeleteBox-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DeleteBox-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DeleteBox-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name box_generator-srv:<DeleteBox-response> is deprecated: use box_generator-srv:DeleteBox-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <DeleteBox-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:success-val is deprecated.  Use box_generator-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <DeleteBox-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader box_generator-srv:message-val is deprecated.  Use box_generator-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DeleteBox-response>) ostream)
  "Serializes a message object of type '<DeleteBox-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DeleteBox-response>) istream)
  "Deserializes a message object of type '<DeleteBox-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DeleteBox-response>)))
  "Returns string type for a service object of type '<DeleteBox-response>"
  "box_generator/DeleteBoxResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DeleteBox-response)))
  "Returns string type for a service object of type 'DeleteBox-response"
  "box_generator/DeleteBoxResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DeleteBox-response>)))
  "Returns md5sum for a message object of type '<DeleteBox-response>"
  "82214afe4ff077ebd4b8aa0c572e1255")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DeleteBox-response)))
  "Returns md5sum for a message object of type 'DeleteBox-response"
  "82214afe4ff077ebd4b8aa0c572e1255")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DeleteBox-response>)))
  "Returns full string definition for message of type '<DeleteBox-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DeleteBox-response)))
  "Returns full string definition for message of type 'DeleteBox-response"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DeleteBox-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DeleteBox-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DeleteBox-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DeleteBox)))
  'DeleteBox-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DeleteBox)))
  'DeleteBox-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DeleteBox)))
  "Returns string type for a service object of type '<DeleteBox>"
  "box_generator/DeleteBox")