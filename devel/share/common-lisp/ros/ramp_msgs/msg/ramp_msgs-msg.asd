
(cl:in-package :asdf)

(defsystem "ramp_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :nav_msgs-msg
               :std_msgs-msg
               :trajectory_msgs-msg
)
  :components ((:file "_package")
    (:file "BezierCurve" :depends-on ("_package_BezierCurve"))
    (:file "_package_BezierCurve" :depends-on ("_package"))
    (:file "Circle" :depends-on ("_package_Circle"))
    (:file "_package_Circle" :depends-on ("_package"))
    (:file "CircleGroup" :depends-on ("_package_CircleGroup"))
    (:file "_package_CircleGroup" :depends-on ("_package"))
    (:file "EvaluationRequest" :depends-on ("_package_EvaluationRequest"))
    (:file "_package_EvaluationRequest" :depends-on ("_package"))
    (:file "EvaluationResponse" :depends-on ("_package_EvaluationResponse"))
    (:file "_package_EvaluationResponse" :depends-on ("_package"))
    (:file "HilbertMap" :depends-on ("_package_HilbertMap"))
    (:file "_package_HilbertMap" :depends-on ("_package"))
    (:file "KnotPoint" :depends-on ("_package_KnotPoint"))
    (:file "_package_KnotPoint" :depends-on ("_package"))
    (:file "MotionState" :depends-on ("_package_MotionState"))
    (:file "_package_MotionState" :depends-on ("_package"))
    (:file "Obstacle" :depends-on ("_package_Obstacle"))
    (:file "_package_Obstacle" :depends-on ("_package"))
    (:file "ObstacleList" :depends-on ("_package_ObstacleList"))
    (:file "_package_ObstacleList" :depends-on ("_package"))
    (:file "PackedObstacle" :depends-on ("_package_PackedObstacle"))
    (:file "_package_PackedObstacle" :depends-on ("_package"))
    (:file "Path" :depends-on ("_package_Path"))
    (:file "_package_Path" :depends-on ("_package"))
    (:file "Population" :depends-on ("_package_Population"))
    (:file "_package_Population" :depends-on ("_package"))
    (:file "RampTrajectory" :depends-on ("_package_RampTrajectory"))
    (:file "_package_RampTrajectory" :depends-on ("_package"))
    (:file "Range" :depends-on ("_package_Range"))
    (:file "_package_Range" :depends-on ("_package"))
    (:file "TrajectoryRequest" :depends-on ("_package_TrajectoryRequest"))
    (:file "_package_TrajectoryRequest" :depends-on ("_package"))
    (:file "TrajectoryResponse" :depends-on ("_package_TrajectoryResponse"))
    (:file "_package_TrajectoryResponse" :depends-on ("_package"))
  ))