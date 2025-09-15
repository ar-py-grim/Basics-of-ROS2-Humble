#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"
#include "example_interfaces/srv/set_bool.hpp"

using std::placeholders:: _1;
using std::placeholders:: _2;


class number_counterNode : public rclcpp::Node 
{
public:
    number_counterNode() : Node("number_counter"),counter(0)
    {
        reset_counter =this->create_service<example_interfaces::srv::SetBool>("reset_counter",
        std::bind(&number_counterNode::callbackbool,this,_1,_2)); 

        publisher = this->create_publisher<example_interfaces::msg::Int64>("number_count", 10);

        timer = this->create_wall_timer(std::chrono::milliseconds(1000),
        std::bind(&number_counterNode::publishData,this));

        subscriber = this->create_subscription<example_interfaces::msg::Int64>("number",10,
        std::bind(&number_counterNode::callBackData,this,
        std::placeholders::_1)); 

        RCLCPP_INFO(this->get_logger(), "phone has started ");
    }

private:
void callBackData(const example_interfaces::msg::Int64::SharedPtr msg){
    RCLCPP_INFO(this->get_logger(), "%ld", msg->data);
  }
  int counter;
void publishData(){
    auto num = example_interfaces::msg::Int64();
        num.data = counter++;
        publisher->publish(num);
    }

void callbackbool(const example_interfaces::srv::SetBool::Request::SharedPtr request,
            const example_interfaces::srv::SetBool::Response::SharedPtr response)
            {
                if(request->data){
                  counter = 0;
                  response->success = true;
                  response->message = "Counter has been reset";
                }
                else{
                    response->success = false;
                    response->message = "Counter has not been reset";
                }
            }
    rclcpp::Service<example_interfaces::srv::SetBool>::SharedPtr reset_counter;
    rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscriber;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher;
    rclcpp::TimerBase::SharedPtr timer;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<number_counterNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}