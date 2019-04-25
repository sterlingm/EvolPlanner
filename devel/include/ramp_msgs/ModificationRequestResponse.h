// Generated by gencpp from file ramp_msgs/ModificationRequestResponse.msg
// DO NOT EDIT!


#ifndef RAMP_MSGS_MESSAGE_MODIFICATIONREQUESTRESPONSE_H
#define RAMP_MSGS_MESSAGE_MODIFICATIONREQUESTRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <ramp_msgs/Path.h>

namespace ramp_msgs
{
template <class ContainerAllocator>
struct ModificationRequestResponse_
{
  typedef ModificationRequestResponse_<ContainerAllocator> Type;

  ModificationRequestResponse_()
    : mod_paths()  {
    }
  ModificationRequestResponse_(const ContainerAllocator& _alloc)
    : mod_paths(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::ramp_msgs::Path_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::ramp_msgs::Path_<ContainerAllocator> >::other >  _mod_paths_type;
  _mod_paths_type mod_paths;





  typedef boost::shared_ptr< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> const> ConstPtr;

}; // struct ModificationRequestResponse_

typedef ::ramp_msgs::ModificationRequestResponse_<std::allocator<void> > ModificationRequestResponse;

typedef boost::shared_ptr< ::ramp_msgs::ModificationRequestResponse > ModificationRequestResponsePtr;
typedef boost::shared_ptr< ::ramp_msgs::ModificationRequestResponse const> ModificationRequestResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ramp_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'ramp_msgs': ['/home/mason/Documents/evol_planner/src/packages/ramp_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "08df06df43e07409d295b8cc678df7cf";
  }

  static const char* value(const ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x08df06df43e07409ULL;
  static const uint64_t static_value2 = 0xd295b8cc678df7cfULL;
};

template<class ContainerAllocator>
struct DataType< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ramp_msgs/ModificationRequestResponse";
  }

  static const char* value(const ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
Path[]  mod_paths\n\
\n\
\n\
================================================================================\n\
MSG: ramp_msgs/Path\n\
ramp_msgs/KnotPoint[] points\n\
\n\
================================================================================\n\
MSG: ramp_msgs/KnotPoint\n\
ramp_msgs/MotionState motionState\n\
uint32 stopTime\n\
\n\
================================================================================\n\
MSG: ramp_msgs/MotionState\n\
float64[] positions\n\
float64[] velocities\n\
float64[] accelerations\n\
float64[] jerks\n\
\n\
# change to duration\n\
float64 time\n\
";
  }

  static const char* value(const ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.mod_paths);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ModificationRequestResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ramp_msgs::ModificationRequestResponse_<ContainerAllocator>& v)
  {
    s << indent << "mod_paths[]" << std::endl;
    for (size_t i = 0; i < v.mod_paths.size(); ++i)
    {
      s << indent << "  mod_paths[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::ramp_msgs::Path_<ContainerAllocator> >::stream(s, indent + "    ", v.mod_paths[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // RAMP_MSGS_MESSAGE_MODIFICATIONREQUESTRESPONSE_H
