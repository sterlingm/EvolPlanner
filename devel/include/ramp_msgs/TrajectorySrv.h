// Generated by gencpp from file ramp_msgs/TrajectorySrv.msg
// DO NOT EDIT!


#ifndef RAMP_MSGS_MESSAGE_TRAJECTORYSRV_H
#define RAMP_MSGS_MESSAGE_TRAJECTORYSRV_H

#include <ros/service_traits.h>


#include <ramp_msgs/TrajectorySrvRequest.h>
#include <ramp_msgs/TrajectorySrvResponse.h>


namespace ramp_msgs
{

struct TrajectorySrv
{

typedef TrajectorySrvRequest Request;
typedef TrajectorySrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct TrajectorySrv
} // namespace ramp_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ramp_msgs::TrajectorySrv > {
  static const char* value()
  {
    return "8ccd59d329076db69674b9c52d4134e4";
  }

  static const char* value(const ::ramp_msgs::TrajectorySrv&) { return value(); }
};

template<>
struct DataType< ::ramp_msgs::TrajectorySrv > {
  static const char* value()
  {
    return "ramp_msgs/TrajectorySrv";
  }

  static const char* value(const ::ramp_msgs::TrajectorySrv&) { return value(); }
};


// service_traits::MD5Sum< ::ramp_msgs::TrajectorySrvRequest> should match 
// service_traits::MD5Sum< ::ramp_msgs::TrajectorySrv > 
template<>
struct MD5Sum< ::ramp_msgs::TrajectorySrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ramp_msgs::TrajectorySrv >::value();
  }
  static const char* value(const ::ramp_msgs::TrajectorySrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ramp_msgs::TrajectorySrvRequest> should match 
// service_traits::DataType< ::ramp_msgs::TrajectorySrv > 
template<>
struct DataType< ::ramp_msgs::TrajectorySrvRequest>
{
  static const char* value()
  {
    return DataType< ::ramp_msgs::TrajectorySrv >::value();
  }
  static const char* value(const ::ramp_msgs::TrajectorySrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ramp_msgs::TrajectorySrvResponse> should match 
// service_traits::MD5Sum< ::ramp_msgs::TrajectorySrv > 
template<>
struct MD5Sum< ::ramp_msgs::TrajectorySrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ramp_msgs::TrajectorySrv >::value();
  }
  static const char* value(const ::ramp_msgs::TrajectorySrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ramp_msgs::TrajectorySrvResponse> should match 
// service_traits::DataType< ::ramp_msgs::TrajectorySrv > 
template<>
struct DataType< ::ramp_msgs::TrajectorySrvResponse>
{
  static const char* value()
  {
    return DataType< ::ramp_msgs::TrajectorySrv >::value();
  }
  static const char* value(const ::ramp_msgs::TrajectorySrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // RAMP_MSGS_MESSAGE_TRAJECTORYSRV_H
