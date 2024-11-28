// Generated by gencpp from file box_generator/MqttListenerResponse.msg
// DO NOT EDIT!


#ifndef BOX_GENERATOR_MESSAGE_MQTTLISTENERRESPONSE_H
#define BOX_GENERATOR_MESSAGE_MQTTLISTENERRESPONSE_H


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
struct MqttListenerResponse_
{
  typedef MqttListenerResponse_<ContainerAllocator> Type;

  MqttListenerResponse_()
    : n_boxes(0)
    , mass(0.0)
    , height(0.0)
    , width(0.0)
    , length(0.0)
    , success(false)
    , status_message()  {
    }
  MqttListenerResponse_(const ContainerAllocator& _alloc)
    : n_boxes(0)
    , mass(0.0)
    , height(0.0)
    , width(0.0)
    , length(0.0)
    , success(false)
    , status_message(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _n_boxes_type;
  _n_boxes_type n_boxes;

   typedef float _mass_type;
  _mass_type mass;

   typedef float _height_type;
  _height_type height;

   typedef float _width_type;
  _width_type width;

   typedef float _length_type;
  _length_type length;

   typedef uint8_t _success_type;
  _success_type success;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _status_message_type;
  _status_message_type status_message;





  typedef boost::shared_ptr< ::box_generator::MqttListenerResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::box_generator::MqttListenerResponse_<ContainerAllocator> const> ConstPtr;

}; // struct MqttListenerResponse_

typedef ::box_generator::MqttListenerResponse_<std::allocator<void> > MqttListenerResponse;

typedef boost::shared_ptr< ::box_generator::MqttListenerResponse > MqttListenerResponsePtr;
typedef boost::shared_ptr< ::box_generator::MqttListenerResponse const> MqttListenerResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::box_generator::MqttListenerResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::box_generator::MqttListenerResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::box_generator::MqttListenerResponse_<ContainerAllocator1> & lhs, const ::box_generator::MqttListenerResponse_<ContainerAllocator2> & rhs)
{
  return lhs.n_boxes == rhs.n_boxes &&
    lhs.mass == rhs.mass &&
    lhs.height == rhs.height &&
    lhs.width == rhs.width &&
    lhs.length == rhs.length &&
    lhs.success == rhs.success &&
    lhs.status_message == rhs.status_message;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::box_generator::MqttListenerResponse_<ContainerAllocator1> & lhs, const ::box_generator::MqttListenerResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace box_generator

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::box_generator::MqttListenerResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::box_generator::MqttListenerResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::box_generator::MqttListenerResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::box_generator::MqttListenerResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::box_generator::MqttListenerResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::box_generator::MqttListenerResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::box_generator::MqttListenerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eca67f62be2b35d15d597743c12e190f";
  }

  static const char* value(const ::box_generator::MqttListenerResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeca67f62be2b35d1ULL;
  static const uint64_t static_value2 = 0x5d597743c12e190fULL;
};

template<class ContainerAllocator>
struct DataType< ::box_generator::MqttListenerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "box_generator/MqttListenerResponse";
  }

  static const char* value(const ::box_generator::MqttListenerResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::box_generator::MqttListenerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 n_boxes\n"
"float32 mass\n"
"float32 height\n"
"float32 width\n"
"float32 length\n"
"bool success\n"
"string status_message\n"
;
  }

  static const char* value(const ::box_generator::MqttListenerResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::box_generator::MqttListenerResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.n_boxes);
      stream.next(m.mass);
      stream.next(m.height);
      stream.next(m.width);
      stream.next(m.length);
      stream.next(m.success);
      stream.next(m.status_message);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MqttListenerResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::box_generator::MqttListenerResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::box_generator::MqttListenerResponse_<ContainerAllocator>& v)
  {
    s << indent << "n_boxes: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.n_boxes);
    s << indent << "mass: ";
    Printer<float>::stream(s, indent + "  ", v.mass);
    s << indent << "height: ";
    Printer<float>::stream(s, indent + "  ", v.height);
    s << indent << "width: ";
    Printer<float>::stream(s, indent + "  ", v.width);
    s << indent << "length: ";
    Printer<float>::stream(s, indent + "  ", v.length);
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
    s << indent << "status_message: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.status_message);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BOX_GENERATOR_MESSAGE_MQTTLISTENERRESPONSE_H
