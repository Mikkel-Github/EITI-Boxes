
(cl:in-package :asdf)

(defsystem "box_generator-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DeleteBox" :depends-on ("_package_DeleteBox"))
    (:file "_package_DeleteBox" :depends-on ("_package"))
    (:file "SpawnBox" :depends-on ("_package_SpawnBox"))
    (:file "_package_SpawnBox" :depends-on ("_package"))
  ))