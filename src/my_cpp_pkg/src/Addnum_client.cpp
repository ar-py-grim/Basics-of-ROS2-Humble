#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

class AddNumClientNode : public rclcpp::Node 
{
public:
    AddNumClientNode() : Node("AddNum") 
    {
      threads.push_back(std::thread(std::bind(&AddNumClientNode::callservice,this,65,78)));
      threads.push_back(std::thread(std::bind(&AddNumClientNode::callservice,this,34,78)));
    }
    void callservice(int64_t a, int64_t b){
        auto client = this->create_client<example_interfaces::srv::AddTwoInts>("AddNum");
        while (!(client->wait_for_service(std::chrono::seconds(1)))){
            RCLCPP_WARN(get_logger(), "waiting for server to be up");
        }
        auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
        request->a = a;
        request->b = b;
        auto future = client->async_send_request(request);
        try{
            auto response = future.get();
            RCLCPP_INFO(get_logger(), "%ld + %ld = %ld",a,b,response->sum);
        }
        catch(std::exception &e){
           RCLCPP_ERROR(get_logger(), "error occured");
        }
    }

private:
     std::vector<std::thread> threads;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddNumClientNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}