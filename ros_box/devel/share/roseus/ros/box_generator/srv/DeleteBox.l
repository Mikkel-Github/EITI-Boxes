;; Auto-generated. Do not edit!


(when (boundp 'box_generator::DeleteBox)
  (if (not (find-package "BOX_GENERATOR"))
    (make-package "BOX_GENERATOR"))
  (shadow 'DeleteBox (find-package "BOX_GENERATOR")))
(unless (find-package "BOX_GENERATOR::DELETEBOX")
  (make-package "BOX_GENERATOR::DELETEBOX"))
(unless (find-package "BOX_GENERATOR::DELETEBOXREQUEST")
  (make-package "BOX_GENERATOR::DELETEBOXREQUEST"))
(unless (find-package "BOX_GENERATOR::DELETEBOXRESPONSE")
  (make-package "BOX_GENERATOR::DELETEBOXRESPONSE"))

(in-package "ROS")





(defclass box_generator::DeleteBoxRequest
  :super ros::object
  :slots (_boxes_id ))

(defmethod box_generator::DeleteBoxRequest
  (:init
   (&key
    ((:boxes_id __boxes_id) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _boxes_id __boxes_id)
   self)
  (:boxes_id
   (&optional __boxes_id)
   (if __boxes_id (setq _boxes_id __boxes_id)) _boxes_id)
  (:serialization-length
   ()
   (+
    ;; string[] _boxes_id
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _boxes_id)) 4
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
   ;;
   self)
  )

(defclass box_generator::DeleteBoxResponse
  :super ros::object
  :slots (_success _message ))

(defmethod box_generator::DeleteBoxResponse
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

(defclass box_generator::DeleteBox
  :super ros::object
  :slots ())

(setf (get box_generator::DeleteBox :md5sum-) "82214afe4ff077ebd4b8aa0c572e1255")
(setf (get box_generator::DeleteBox :datatype-) "box_generator/DeleteBox")
(setf (get box_generator::DeleteBox :request) box_generator::DeleteBoxRequest)
(setf (get box_generator::DeleteBox :response) box_generator::DeleteBoxResponse)

(defmethod box_generator::DeleteBoxRequest
  (:response () (instance box_generator::DeleteBoxResponse :init)))

(setf (get box_generator::DeleteBoxRequest :md5sum-) "82214afe4ff077ebd4b8aa0c572e1255")
(setf (get box_generator::DeleteBoxRequest :datatype-) "box_generator/DeleteBoxRequest")
(setf (get box_generator::DeleteBoxRequest :definition-)
      "string[] boxes_id
---
bool success
string message
")

(setf (get box_generator::DeleteBoxResponse :md5sum-) "82214afe4ff077ebd4b8aa0c572e1255")
(setf (get box_generator::DeleteBoxResponse :datatype-) "box_generator/DeleteBoxResponse")
(setf (get box_generator::DeleteBoxResponse :definition-)
      "string[] boxes_id
---
bool success
string message
")



(provide :box_generator/DeleteBox "82214afe4ff077ebd4b8aa0c572e1255")


