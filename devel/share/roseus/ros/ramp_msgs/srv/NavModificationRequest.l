;; Auto-generated. Do not edit!


(when (boundp 'ramp_msgs::NavModificationRequest)
  (if (not (find-package "RAMP_MSGS"))
    (make-package "RAMP_MSGS"))
  (shadow 'NavModificationRequest (find-package "RAMP_MSGS")))
(unless (find-package "RAMP_MSGS::NAVMODIFICATIONREQUEST")
  (make-package "RAMP_MSGS::NAVMODIFICATIONREQUEST"))
(unless (find-package "RAMP_MSGS::NAVMODIFICATIONREQUESTREQUEST")
  (make-package "RAMP_MSGS::NAVMODIFICATIONREQUESTREQUEST"))
(unless (find-package "RAMP_MSGS::NAVMODIFICATIONREQUESTRESPONSE")
  (make-package "RAMP_MSGS::NAVMODIFICATIONREQUESTRESPONSE"))

(in-package "ROS")

(if (not (find-package "NAV_MSGS"))
  (ros::roseus-add-msgs "nav_msgs"))


(if (not (find-package "NAV_MSGS"))
  (ros::roseus-add-msgs "nav_msgs"))


(defclass ramp_msgs::NavModificationRequestRequest
  :super ros::object
  :slots (_paths _op _repair_dist _repair_dir _repair_ob_r ))

(defmethod ramp_msgs::NavModificationRequestRequest
  (:init
   (&key
    ((:paths __paths) (let (r) (dotimes (i 0) (push (instance nav_msgs::Path :init) r)) r))
    ((:op __op) "")
    ((:repair_dist __repair_dist) 0.0)
    ((:repair_dir __repair_dir) 0.0)
    ((:repair_ob_r __repair_ob_r) 0.0)
    )
   (send-super :init)
   (setq _paths __paths)
   (setq _op (string __op))
   (setq _repair_dist (float __repair_dist))
   (setq _repair_dir (float __repair_dir))
   (setq _repair_ob_r (float __repair_ob_r))
   self)
  (:paths
   (&rest __paths)
   (if (keywordp (car __paths))
       (send* _paths __paths)
     (progn
       (if __paths (setq _paths (car __paths)))
       _paths)))
  (:op
   (&optional __op)
   (if __op (setq _op __op)) _op)
  (:repair_dist
   (&optional __repair_dist)
   (if __repair_dist (setq _repair_dist __repair_dist)) _repair_dist)
  (:repair_dir
   (&optional __repair_dir)
   (if __repair_dir (setq _repair_dir __repair_dir)) _repair_dir)
  (:repair_ob_r
   (&optional __repair_ob_r)
   (if __repair_ob_r (setq _repair_ob_r __repair_ob_r)) _repair_ob_r)
  (:serialization-length
   ()
   (+
    ;; nav_msgs/Path[] _paths
    (apply #'+ (send-all _paths :serialization-length)) 4
    ;; string _op
    4 (length _op)
    ;; float64 _repair_dist
    8
    ;; float64 _repair_dir
    8
    ;; float64 _repair_ob_r
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; nav_msgs/Path[] _paths
     (write-long (length _paths) s)
     (dolist (elem _paths)
       (send elem :serialize s)
       )
     ;; string _op
       (write-long (length _op) s) (princ _op s)
     ;; float64 _repair_dist
       (sys::poke _repair_dist (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _repair_dir
       (sys::poke _repair_dir (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _repair_ob_r
       (sys::poke _repair_ob_r (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; nav_msgs/Path[] _paths
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _paths (let (r) (dotimes (i n) (push (instance nav_msgs::Path :init) r)) r))
     (dolist (elem- _paths)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; string _op
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _op (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _repair_dist
     (setq _repair_dist (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _repair_dir
     (setq _repair_dir (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _repair_ob_r
     (setq _repair_ob_r (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass ramp_msgs::NavModificationRequestResponse
  :super ros::object
  :slots (_mod_paths ))

(defmethod ramp_msgs::NavModificationRequestResponse
  (:init
   (&key
    ((:mod_paths __mod_paths) (let (r) (dotimes (i 0) (push (instance nav_msgs::Path :init) r)) r))
    )
   (send-super :init)
   (setq _mod_paths __mod_paths)
   self)
  (:mod_paths
   (&rest __mod_paths)
   (if (keywordp (car __mod_paths))
       (send* _mod_paths __mod_paths)
     (progn
       (if __mod_paths (setq _mod_paths (car __mod_paths)))
       _mod_paths)))
  (:serialization-length
   ()
   (+
    ;; nav_msgs/Path[] _mod_paths
    (apply #'+ (send-all _mod_paths :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; nav_msgs/Path[] _mod_paths
     (write-long (length _mod_paths) s)
     (dolist (elem _mod_paths)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; nav_msgs/Path[] _mod_paths
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _mod_paths (let (r) (dotimes (i n) (push (instance nav_msgs::Path :init) r)) r))
     (dolist (elem- _mod_paths)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(defclass ramp_msgs::NavModificationRequest
  :super ros::object
  :slots ())

(setf (get ramp_msgs::NavModificationRequest :md5sum-) "3811dc7a15f462d593d653ffa9b613c5")
(setf (get ramp_msgs::NavModificationRequest :datatype-) "ramp_msgs/NavModificationRequest")
(setf (get ramp_msgs::NavModificationRequest :request) ramp_msgs::NavModificationRequestRequest)
(setf (get ramp_msgs::NavModificationRequest :response) ramp_msgs::NavModificationRequestResponse)

(defmethod ramp_msgs::NavModificationRequestRequest
  (:response () (instance ramp_msgs::NavModificationRequestResponse :init)))

(setf (get ramp_msgs::NavModificationRequestRequest :md5sum-) "3811dc7a15f462d593d653ffa9b613c5")
(setf (get ramp_msgs::NavModificationRequestRequest :datatype-) "ramp_msgs/NavModificationRequestRequest")
(setf (get ramp_msgs::NavModificationRequestRequest :definition-)
      "nav_msgs/Path[] paths
string op
float64 repair_dist
float64 repair_dir
float64 repair_ob_r


================================================================================
MSG: nav_msgs/Path
#An array of poses that represents a Path for a robot to follow
Header header
geometry_msgs/PoseStamped[] poses

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
---

nav_msgs/Path[]  mod_paths


================================================================================
MSG: nav_msgs/Path
#An array of poses that represents a Path for a robot to follow
Header header
geometry_msgs/PoseStamped[] poses

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
")

(setf (get ramp_msgs::NavModificationRequestResponse :md5sum-) "3811dc7a15f462d593d653ffa9b613c5")
(setf (get ramp_msgs::NavModificationRequestResponse :datatype-) "ramp_msgs/NavModificationRequestResponse")
(setf (get ramp_msgs::NavModificationRequestResponse :definition-)
      "nav_msgs/Path[] paths
string op
float64 repair_dist
float64 repair_dir
float64 repair_ob_r


================================================================================
MSG: nav_msgs/Path
#An array of poses that represents a Path for a robot to follow
Header header
geometry_msgs/PoseStamped[] poses

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
---

nav_msgs/Path[]  mod_paths


================================================================================
MSG: nav_msgs/Path
#An array of poses that represents a Path for a robot to follow
Header header
geometry_msgs/PoseStamped[] poses

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
")



(provide :ramp_msgs/NavModificationRequest "3811dc7a15f462d593d653ffa9b613c5")


