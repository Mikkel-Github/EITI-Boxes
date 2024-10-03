;; Auto-generated. Do not edit!


(when (boundp 'box_generator::SpawnBox)
  (if (not (find-package "BOX_GENERATOR"))
    (make-package "BOX_GENERATOR"))
  (shadow 'SpawnBox (find-package "BOX_GENERATOR")))
(unless (find-package "BOX_GENERATOR::SPAWNBOX")
  (make-package "BOX_GENERATOR::SPAWNBOX"))
(unless (find-package "BOX_GENERATOR::SPAWNBOXREQUEST")
  (make-package "BOX_GENERATOR::SPAWNBOXREQUEST"))
(unless (find-package "BOX_GENERATOR::SPAWNBOXRESPONSE")
  (make-package "BOX_GENERATOR::SPAWNBOXRESPONSE"))

(in-package "ROS")





(defclass box_generator::SpawnBoxRequest
  :super ros::object
  :slots (_boxes_id _mass _length _width _height ))

(defmethod box_generator::SpawnBoxRequest
  (:init
   (&key
    ((:boxes_id __boxes_id) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:mass __mass) 0.0)
    ((:length __length) 0.0)
    ((:width __width) 0.0)
    ((:height __height) 0.0)
    )
   (send-super :init)
   (setq _boxes_id __boxes_id)
   (setq _mass (float __mass))
   (setq _length (float __length))
   (setq _width (float __width))
   (setq _height (float __height))
   self)
  (:boxes_id
   (&optional __boxes_id)
   (if __boxes_id (setq _boxes_id __boxes_id)) _boxes_id)
  (:mass
   (&optional __mass)
   (if __mass (setq _mass __mass)) _mass)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:serialization-length
   ()
   (+
    ;; string[] _boxes_id
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _boxes_id)) 4
    ;; float32 _mass
    4
    ;; float32 _length
    4
    ;; float32 _width
    4
    ;; float32 _height
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _boxes_id
     (write-long (length _boxes_id) s)
     (dolist (elem _boxes_id)
       (write-long (length elem) s) (princ elem s)
       )
     ;; float32 _mass
       (sys::poke _mass (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _length
       (sys::poke _length (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _width
       (sys::poke _width (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _height
       (sys::poke _height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _boxes_id
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _boxes_id (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _boxes_id i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; float32 _mass
     (setq _mass (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _length
     (setq _length (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _width
     (setq _width (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass box_generator::SpawnBoxResponse
  :super ros::object
  :slots (_success _status_message ))

(defmethod box_generator::SpawnBoxResponse
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

(defclass box_generator::SpawnBox
  :super ros::object
  :slots ())

(setf (get box_generator::SpawnBox :md5sum-) "45a1e59f6217c34ce24acbd9cc8ec4e3")
(setf (get box_generator::SpawnBox :datatype-) "box_generator/SpawnBox")
(setf (get box_generator::SpawnBox :request) box_generator::SpawnBoxRequest)
(setf (get box_generator::SpawnBox :response) box_generator::SpawnBoxResponse)

(defmethod box_generator::SpawnBoxRequest
  (:response () (instance box_generator::SpawnBoxResponse :init)))

(setf (get box_generator::SpawnBoxRequest :md5sum-) "45a1e59f6217c34ce24acbd9cc8ec4e3")
(setf (get box_generator::SpawnBoxRequest :datatype-) "box_generator/SpawnBoxRequest")
(setf (get box_generator::SpawnBoxRequest :definition-)
      "string[] boxes_id
float32 mass
float32 length
float32 width
float32 height
---
bool success
string status_message

")

(setf (get box_generator::SpawnBoxResponse :md5sum-) "45a1e59f6217c34ce24acbd9cc8ec4e3")
(setf (get box_generator::SpawnBoxResponse :datatype-) "box_generator/SpawnBoxResponse")
(setf (get box_generator::SpawnBoxResponse :definition-)
      "string[] boxes_id
float32 mass
float32 length
float32 width
float32 height
---
bool success
string status_message

")



(provide :box_generator/SpawnBox "45a1e59f6217c34ce24acbd9cc8ec4e3")


