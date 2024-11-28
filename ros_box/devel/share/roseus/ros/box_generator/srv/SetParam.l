;; Auto-generated. Do not edit!


(when (boundp 'box_generator::SetParam)
  (if (not (find-package "BOX_GENERATOR"))
    (make-package "BOX_GENERATOR"))
  (shadow 'SetParam (find-package "BOX_GENERATOR")))
(unless (find-package "BOX_GENERATOR::SETPARAM")
  (make-package "BOX_GENERATOR::SETPARAM"))
(unless (find-package "BOX_GENERATOR::SETPARAMREQUEST")
  (make-package "BOX_GENERATOR::SETPARAMREQUEST"))
(unless (find-package "BOX_GENERATOR::SETPARAMRESPONSE")
  (make-package "BOX_GENERATOR::SETPARAMRESPONSE"))

(in-package "ROS")





(defclass box_generator::SetParamRequest
  :super ros::object
  :slots (_max_speed_xy _max_vel_x _acc_lim_x _decel_lim_x _max_vel_theta ))

(defmethod box_generator::SetParamRequest
  (:init
   (&key
    ((:max_speed_xy __max_speed_xy) 0.0)
    ((:max_vel_x __max_vel_x) 0.0)
    ((:acc_lim_x __acc_lim_x) 0.0)
    ((:decel_lim_x __decel_lim_x) 0.0)
    ((:max_vel_theta __max_vel_theta) 0.0)
    )
   (send-super :init)
   (setq _max_speed_xy (float __max_speed_xy))
   (setq _max_vel_x (float __max_vel_x))
   (setq _acc_lim_x (float __acc_lim_x))
   (setq _decel_lim_x (float __decel_lim_x))
   (setq _max_vel_theta (float __max_vel_theta))
   self)
  (:max_speed_xy
   (&optional __max_speed_xy)
   (if __max_speed_xy (setq _max_speed_xy __max_speed_xy)) _max_speed_xy)
  (:max_vel_x
   (&optional __max_vel_x)
   (if __max_vel_x (setq _max_vel_x __max_vel_x)) _max_vel_x)
  (:acc_lim_x
   (&optional __acc_lim_x)
   (if __acc_lim_x (setq _acc_lim_x __acc_lim_x)) _acc_lim_x)
  (:decel_lim_x
   (&optional __decel_lim_x)
   (if __decel_lim_x (setq _decel_lim_x __decel_lim_x)) _decel_lim_x)
  (:max_vel_theta
   (&optional __max_vel_theta)
   (if __max_vel_theta (setq _max_vel_theta __max_vel_theta)) _max_vel_theta)
  (:serialization-length
   ()
   (+
    ;; float32 _max_speed_xy
    4
    ;; float32 _max_vel_x
    4
    ;; float32 _acc_lim_x
    4
    ;; float32 _decel_lim_x
    4
    ;; float32 _max_vel_theta
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _max_speed_xy
       (sys::poke _max_speed_xy (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _max_vel_x
       (sys::poke _max_vel_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acc_lim_x
       (sys::poke _acc_lim_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _decel_lim_x
       (sys::poke _decel_lim_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _max_vel_theta
       (sys::poke _max_vel_theta (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _max_speed_xy
     (setq _max_speed_xy (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _max_vel_x
     (setq _max_vel_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acc_lim_x
     (setq _acc_lim_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _decel_lim_x
     (setq _decel_lim_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _max_vel_theta
     (setq _max_vel_theta (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass box_generator::SetParamResponse
  :super ros::object
  :slots (_success _status_message ))

(defmethod box_generator::SetParamResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:status_message __status_message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _status_message (string __status_message))
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:status_message
   (&optional __status_message)
   (if __status_message (setq _status_message __status_message)) _status_message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _status_message
    4 (length _status_message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _status_message
       (write-long (length _status_message) s) (princ _status_message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _status_message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _status_message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass box_generator::SetParam
  :super ros::object
  :slots ())

(setf (get box_generator::SetParam :md5sum-) "3e7c329fec6fea0b39dd75f575b3c45d")
(setf (get box_generator::SetParam :datatype-) "box_generator/SetParam")
(setf (get box_generator::SetParam :request) box_generator::SetParamRequest)
(setf (get box_generator::SetParam :response) box_generator::SetParamResponse)

(defmethod box_generator::SetParamRequest
  (:response () (instance box_generator::SetParamResponse :init)))

(setf (get box_generator::SetParamRequest :md5sum-) "3e7c329fec6fea0b39dd75f575b3c45d")
(setf (get box_generator::SetParamRequest :datatype-) "box_generator/SetParamRequest")
(setf (get box_generator::SetParamRequest :definition-)
      "float32 max_speed_xy
float32 max_vel_x
float32 acc_lim_x
float32 decel_lim_x
float32 max_vel_theta
---
bool success
string status_message

")

(setf (get box_generator::SetParamResponse :md5sum-) "3e7c329fec6fea0b39dd75f575b3c45d")
(setf (get box_generator::SetParamResponse :datatype-) "box_generator/SetParamResponse")
(setf (get box_generator::SetParamResponse :definition-)
      "float32 max_speed_xy
float32 max_vel_x
float32 acc_lim_x
float32 decel_lim_x
float32 max_vel_theta
---
bool success
string status_message

")



(provide :box_generator/SetParam "3e7c329fec6fea0b39dd75f575b3c45d")


