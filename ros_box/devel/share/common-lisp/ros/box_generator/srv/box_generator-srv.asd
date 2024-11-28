
(cl:in-package :asdf)

(defsystem "box_generator-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "BoxPlacer" :depends-on ("_package_BoxPlacer"))
    (:file "_package_BoxPlacer" :depends-on ("_package"))
    (:file "DeleteBox" :depends-on ("_package_DeleteBox"))
    (:file "_package_DeleteBox" :depends-on ("_package"))
    (:file "SetParam" :depends-on ("_package_SetParam"))
    (:file "_package_SetParam" :depends-on ("_package"))
    (:file "SpawnBox" :depends-on ("_package_SpawnBox"))
    (:file "_package_SpawnBox" :depends-on ("_package"))
  ))