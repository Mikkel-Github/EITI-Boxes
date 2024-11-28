;; Auto-generated. Do not edit!


(when (boundp 'box_generator::MqttListener)
  (if (not (find-package "BOX_GENERATOR"))
    (make-package "BOX_GENERATOR"))
  (shadow 'MqttListener (find-package "BOX_GENERATOR")))
(unless (find-package "BOX_GENERATOR::MQTTLISTENER")
  (make-package "BOX_GENERATOR::MQTTLISTENER"))
(unless (find-package "BOX_GENERATOR::MQTTLISTENERREQUEST")
  (make-package "BOX_GENERATOR::MQTTLISTENERREQUEST"))
(unless (find-package "BOX_GENERATOR::MQTTLISTENERRESPONSE")
  (make-package "BOX_GENERATOR::MQTTLISTENERRESPONSE"))

(in-package "ROS")





(defclass box_generator::MqttListenerRequest
  :super ros::object
  :slots ())

(defmethod box_generator::MqttListenerRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass box_generator::MqttListenerResponse
  :super ros::object
  :slots (_n_boxes _mass _height _width _length _success _status_message ))

(defmethod box_generator::MqttListenerResponse
  (:init
   (&key
    ((:n_boxes __n_boxes) 0)
    ((:mass __mass) 0.0)
    ((:height __height) 0.0)
    ((:width __width) 0.0)
    ((:length __length) 0.0)
    ((:success __success) nil)
    ((:status_message __status_message) "")
    )
   (send-super :init)
   (setq _n_boxes (round __n_boxes))
   (setq _mass (float __mass))
   (setq _height (float __height))
   (setq _width (float __width))
   (setq _length (float __length))
   (setq _success __success)
   (setq _status_message (string __status_message))
   self)
  (:n_boxes
   (&optional __n_boxes)
   (if __n_boxes (setq _n_boxes __n_boxes)) _n_boxes)
  (:mass
   (&optional __mass)
   (if __mass (setq _mass __mass)) _mass)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:status_message
   (&optional __status_message)
   (if __status_message (setq _status_message __status_message)) _status_message)
  (:serialization-length
   ()
   (+
    ;; uint8 _n_boxes
    1
    ;; float32 _mass
    4
    ;; float32 _height
    4
    ;; float32 _width
    4
    ;; float32 _length
    4
    ;; bool _success
    1
    ;; string _status_message
    4 (length _status_message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _n_boxes
       (write-byte _n_boxes s)
     ;; float32 _mass
       (sys::poke _mass (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _height
       (sys::poke _height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _width
       (sys::poke _width (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _length
       (sys::poke _length (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _status_message
       (write-long (length _status_message) s) (princ _status_message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _n_boxes
     (setq _n_boxes (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _mass
     (setq _mass (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _width
     (setq _width (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _length
     (setq _length (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _status_message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _status_message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass box_generator::MqttListener
  :super ros::object
  :slots ())

(setf (get box_generator::MqttListener :md5sum-) "eca67f62be2b35d15d597743c12e190f")
(setf (get box_generator::MqttListener :datatype-) "box_generator/MqttListener")
(setf (get box_generator::MqttListener :request) box_generator::MqttListenerRequest)
(setf (get box_generator::MqttListener :response) box_generator::MqttListenerResponse)

(defmethod box_generator::MqttListenerRequest
  (:response () (instance box_generator::MqttListenerResponse :init)))

(setf (get box_generator::MqttListenerRequest :md5sum-) "eca67f62be2b35d15d597743c12e190f")
(setf (get box_generator::MqttListenerRequest :datatype-) "box_generator/MqttListenerRequest")
(setf (get box_generator::MqttListenerRequest :definition-)
      "
---
uint8 n_boxes
float32 mass
float32 height
float32 width
float32 length
bool success
string status_message
")

(setf (get box_generator::MqttListenerResponse :md5sum-) "eca67f62be2b35d15d597743c12e190f")
(setf (get box_generator::MqttListenerResponse :datatype-) "box_generator/MqttListenerResponse")
(setf (get box_generator::MqttListenerResponse :definition-)
      "
---
uint8 n_boxes
float32 mass
float32 height
float32 width
float32 length
bool success
string status_message
")



(provide :box_generator/MqttListener "eca67f62be2b35d15d597743c12e190f")

