#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

using std::placeholders:: _1;
using std::placeholders:: _2;

class AddNumNode : public rclcpp::Node 
{
public:
    AddNumNode() : Node("AddNum") 
    {
      server = this->create_service<example_interfaces::srv::AddTwoInts>("AddNum",
      std::bind(&AddNumNode::callbacksum,this,_1,_2));
       RCLCPP_INFO(this->get_logger(),"server is online");
    }

private:
    void callbacksum(const example_interfaces::srv::AddTwoInts::Request::SharedPtr request,
            const example_interfaces::srv::AddTwoInts::Response::SharedPtr response)
            {
                 response->sum = request->a + request->b;
                 RCLCPP_INFO(this->get_logger(), "%ld + %ld = %ld", 
                            request->a,request->b,response->sum);
            }
    rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr server;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddNumNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}