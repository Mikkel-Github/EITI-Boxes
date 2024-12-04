;; Auto-generated. Do not edit!


(when (boundp 'box_generator::WaypointSender)
  (if (not (find-package "BOX_GENERATOR"))
    (make-package "BOX_GENERATOR"))
  (shadow 'WaypointSender (find-package "BOX_GENERATOR")))
(unless (find-package "BOX_GENERATOR::WAYPOINTSENDER")
  (make-package "BOX_GENERATOR::WAYPOINTSENDER"))
(unless (find-package "BOX_GENERATOR::WAYPOINTSENDERREQUEST")
  (make-package "BOX_GENERATOR::WAYPOINTSENDERREQUEST"))
(unless (find-package "BOX_GENERATOR::WAYPOINTSENDERRESPONSE")
  (make-package "BOX_GENERATOR::WAYPOINTSENDERRESPONSE"))

(in-package "ROS")





(defclass box_generator::WaypointSenderRequest
  :super ros::object
  :slots (_position_x _position_y _position_z _orientation_x _orientation_y _orientation_z _orientation_w ))

(defmethod box_generator::WaypointSenderRequest
  (:init
   (&key
    ((:position_x __position_x) 0.0)
    ((:position_y __position_y) 0.0)
    ((:position_z __position_z) 0.0)
    ((:orientation_x __orientation_x) 0.0)
    ((:orientation_y __orientation_y) 0.0)
    ((:orientation_z __orientation_z) 0.0)
    ((:orientation_w __orientation_w) 0.0)
    )
   (send-super :init)
   (setq _position_x (float __position_x))
   (setq _position_y (float __position_y))
   (setq _position_z (float __position_z))
   (setq _orientation_x (float __orientation_x))
   (setq _orientation_y (float __orientation_y))
   (setq _orientation_z (float __orientation_z))
   (setq _orientation_w (float __orientation_w))
   self)
  (:position_x
   (&optional __position_x)
   (if __position_x (setq _position_x __position_x)) _position_x)
  (:position_y
   (&optional __position_y)
   (if __position_y (setq _position_y __position_y)) _position_y)
  (:position_z
   (&optional __position_z)
   (if __position_z (setq _position_z __position_z)) _position_z)
  (:orientation_x
   (&optional __orientation_x)
   (if __orientation_x (setq _orientation_x __orientation_x)) _orientation_x)
  (:orientation_y
   (&optional __orientation_y)
   (if __orientation_y (setq _orientation_y __orientation_y)) _orientation_y)
  (:orientation_z
   (&optional __orientation_z)
   (if __orientation_z (setq _orientation_z __orientation_z)) _orientation_z)
  (:orientation_w
   (&optional __orientation_w)
   (if __orientation_w (setq _orientation_w __orientation_w)) _orientation_w)
  (:serialization-length
   ()
   (+
    ;; float64 _position_x
    8
    ;; float64 _position_y
    8
    ;; float64 _position_z
    8
    ;; float64 _orientation_x
    8
    ;; float64 _orientation_y
    8
    ;; float64 _orientation_z
    8
    ;; float64 _orientation_w
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _position_x
       (sys::poke _position_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _position_y
       (sys::poke _position_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _position_z
       (sys::poke _position_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _orientation_x
       (sys::poke _orientation_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _orientation_y
       (sys::poke _orientation_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _orientation_z
       (sys::poke _orientation_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _orientation_w
       (sys::poke _orientation_w (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _position_x
     (setq _position_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _position_y
     (setq _position_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _position_z
     (setq _position_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _orientation_x
     (setq _orientation_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _orientation_y
     (setq _orientation_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _orientation_z
     (setq _orientation_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _orientation_w
     (setq _orientation_w (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass box_generator::WaypointSenderResponse
  :super ros::object
  :slots (_success _message ))

(defmethod box_generator::WaypointSenderResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass box_generator::WaypointSender
  :super ros::object
  :slots ())

(setf (get box_generator::WaypointSender :md5sum-) "551b10962421931d26e170ffc7184147")
(setf (get box_generator::WaypointSender :datatype-) "box_generator/WaypointSender")
(setf (get box_generator::WaypointSender :request) box_generator::WaypointSenderRequest)
(setf (get box_generator::WaypointSender :response) box_generator::WaypointSenderResponse)

(defmethod box_generator::WaypointSenderRequest
  (:response () (instance box_generator::WaypointSenderResponse :init)))

(setf (get box_generator::WaypointSenderRequest :md5sum-) "551b10962421931d26e170ffc7184147")
(setf (get box_generator::WaypointSenderRequest :datatype-) "box_generator/WaypointSenderRequest")
(setf (get box_generator::WaypointSenderRequest :definition-)
      "# Request
float64 position_x
float64 position_y
float64 position_z
float64 orientation_x
float64 orientation_y
float64 orientation_z
float64 orientation_w

---
# Response
bool success
string message
")

(setf (get box_generator::WaypointSenderResponse :md5sum-) "551b10962421931d26e170ffc7184147")
(setf (get box_generator::WaypointSenderResponse :datatype-) "box_generator/WaypointSenderResponse")
(setf (get box_generator::WaypointSenderResponse :definition-)
      "# Request
float64 position_x
float64 position_y
float64 position_z
float64 orientation_x
float64 orientation_y
float64 orientation_z
float64 orientation_w

---
# Response
bool success
string message
")



(provide :box_generator/WaypointSender "551b10962421931d26e170ffc7184147")


