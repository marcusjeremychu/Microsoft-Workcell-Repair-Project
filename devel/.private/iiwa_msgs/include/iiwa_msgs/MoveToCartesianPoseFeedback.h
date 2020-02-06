// Generated by gencpp from file iiwa_msgs/MoveToCartesianPoseFeedback.msg
// DO NOT EDIT!


#ifndef IIWA_MSGS_MESSAGE_MOVETOCARTESIANPOSEFEEDBACK_H
#define IIWA_MSGS_MESSAGE_MOVETOCARTESIANPOSEFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace iiwa_msgs
{
template <class ContainerAllocator>
struct MoveToCartesianPoseFeedback_
{
  typedef MoveToCartesianPoseFeedback_<ContainerAllocator> Type;

  MoveToCartesianPoseFeedback_()
    {
    }
  MoveToCartesianPoseFeedback_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct MoveToCartesianPoseFeedback_

typedef ::iiwa_msgs::MoveToCartesianPoseFeedback_<std::allocator<void> > MoveToCartesianPoseFeedback;

typedef boost::shared_ptr< ::iiwa_msgs::MoveToCartesianPoseFeedback > MoveToCartesianPoseFeedbackPtr;
typedef boost::shared_ptr< ::iiwa_msgs::MoveToCartesianPoseFeedback const> MoveToCartesianPoseFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace iiwa_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'iiwa_msgs': ['/home/workcell/Desktop/iiwa_stack_ws/src/iiwa_stack/iiwa_msgs/msg', '/home/workcell/Desktop/iiwa_stack_ws/devel/.private/iiwa_msgs/share/iiwa_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "iiwa_msgs/MoveToCartesianPoseFeedback";
  }

  static const char* value(const ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Feedback\n\
\n\
";
  }

  static const char* value(const ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveToCartesianPoseFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::iiwa_msgs::MoveToCartesianPoseFeedback_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // IIWA_MSGS_MESSAGE_MOVETOCARTESIANPOSEFEEDBACK_H
