// Generated by gencpp from file box_generator/MqttRequest.msg
// DO NOT EDIT!


#ifndef BOX_GENERATOR_MESSAGE_MQTTREQUEST_H
#define BOX_GENERATOR_MESSAGE_MQTTREQUEST_H

#include <ros/service_traits.h>


#include <box_generator/MqttRequestRequest.h>
#include <box_generator/MqttRequestResponse.h>


namespace box_generator
{

struct MqttRequest
{

typedef MqttRequestRequest Request;
typedef MqttRequestResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MqttRequest
} // namespace box_generator


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::box_generator::MqttRequest > {
  static const char* value()
  {
    return "eca67f62be2b35d15d597743c12e190f";
  }

  static const char* value(const ::box_generator::MqttRequest&) { return value(); }
};

template<>
struct DataType< ::box_generator::MqttRequest > {
  static const char* value()
  {
    return "box_generator/MqttRequest";
  }

  static const char* value(const ::box_generator::MqttRequest&) { return value(); }
};


// service_traits::MD5Sum< ::box_generator::MqttRequestRequest> should match
// service_traits::MD5Sum< ::box_generator::MqttRequest >
template<>
struct MD5Sum< ::box_generator::MqttRequestRequest>
{
  static const char* value()
  {
    return MD5Sum< ::box_generator::MqttRequest >::value();
  }
  static const char* value(const ::box_generator::MqttRequestRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::box_generator::MqttRequestRequest> should match
// service_traits::DataType< ::box_generator::MqttRequest >
template<>
struct DataType< ::box_generator::MqttRequestRequest>
{
  static const char* value()
  {
    return DataType< ::box_generator::MqttRequest >::value();
  }
  static const char* value(const ::box_generator::MqttRequestRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::box_generator::MqttRequestResponse> should match
// service_traits::MD5Sum< ::box_generator::MqttRequest >
template<>
struct MD5Sum< ::box_generator::MqttRequestResponse>
{
  static const char* value()
  {
    return MD5Sum< ::box_generator::MqttRequest >::value();
  }
  static const char* value(const ::box_generator::MqttRequestResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::box_generator::MqttRequestResponse> should match
// service_traits::DataType< ::box_generator::MqttRequest >
template<>
struct DataType< ::box_generator::MqttRequestResponse>
{
  static const char* value()
  {
    return DataType< ::box_generator::MqttRequest >::value();
  }
  static const char* value(const ::box_generator::MqttRequestResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // BOX_GENERATOR_MESSAGE_MQTTREQUEST_H