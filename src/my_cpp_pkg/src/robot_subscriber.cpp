#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class phoneNode : public rclcpp::Node 
{
public:
    phoneNode() : Node("phone")
    {
        subscriber = this->create_subscription<example_interfaces::msg::String>("robot_news",10,
        std::bind(&phoneNode::callBackRobotNews,this,
        std::placeholders::_1)); 
        RCLCPP_INFO(this->get_logger(), "phone has started ");
    }

private:
  void callBackRobotNews(const example_interfaces::msg::String::SharedPtr msg){
    RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());
  }
  rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<phoneNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}