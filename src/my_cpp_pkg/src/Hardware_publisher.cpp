#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

class HwstatuspublsihNode : public rclcpp::Node 
{
public:
    HwstatuspublsihNode() : Node("hw_status") 
    {
        publisher = this->create_publisher<my_robot_interfaces::msg::HardwareStatus>
                       ("hw_status",10);
        timer = this->create_wall_timer(std::chrono::milliseconds(1000),
        std::bind(&HwstatuspublsihNode::PublishNews,this));
        RCLCPP_INFO(this ->get_logger(),"Transmission started");
    }

private:
void PublishNews(){
        auto msg = my_robot_interfaces::msg::HardwareStatus();
        msg.temperature = 50;
        msg.are_motors_ready = true;
        msg.debug_message = "Nothing here :)";
        publisher->publish(msg);
    }
      rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr publisher;
      rclcpp::TimerBase::SharedPtr timer;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<HwstatuspublsihNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}