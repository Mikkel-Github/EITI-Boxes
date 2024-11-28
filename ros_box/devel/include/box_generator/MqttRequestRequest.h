// Generated by gencpp from file box_generator/MqttRequestRequest.msg
// DO NOT EDIT!


#ifndef BOX_GENERATOR_MESSAGE_MQTTREQUESTREQUEST_H
#define BOX_GENERATOR_MESSAGE_MQTTREQUESTREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace box_generator
{
template <class ContainerAllocator>
struct MqttRequestRequest_
{
  typedef MqttRequestRequest_<ContainerAllocator> Type;

  MqttRequestRequest_()
    {
    }
  MqttRequestRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::box_generator::MqttRequestRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::box_generator::MqttRequestRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MqttRequestRequest_

typedef ::box_generator::MqttRequestRequest_<std::allocator<void> > MqttRequestRequest;

typedef boost::shared_ptr< ::box_generator::MqttRequestRequest > MqttRequestRequestPtr;
typedef boost::shared_ptr< ::box_generator::MqttRequestRequest const> MqttRequestRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::box_generator::MqttRequestRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::box_generator::MqttRequestRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace box_generator

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::box_generator::MqttRequestRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::box_generator::MqttRequestRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::box_generator::MqttRequestRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::box_generator::MqttRequestRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::box_generator::MqttRequestRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::box_generator::MqttRequestRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::box_generator::MqttRequestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::box_generator::MqttRequestRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::box_generator::MqttRequestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "box_generator/MqttRequestRequest";
  }

  static const char* value(const ::box_generator::MqttRequestRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::box_generator::MqttRequestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::box_generator::MqttRequestRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::box_generator::MqttRequestRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MqttRequestRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::box_generator::MqttRequestRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::box_generator::MqttRequestRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // BOX_GENERATOR_MESSAGE_MQTTREQUESTREQUEST_H