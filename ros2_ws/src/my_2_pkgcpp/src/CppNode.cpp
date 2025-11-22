#include "rclcpp/rclcpp.hpp"

int main(int argc , char** argv){
    rclcpp::init(argc,argv);
    auto node = std::make_shared<rclcpp::Node>("Node1");
    RCLCPP_INFO(node->get_logger(),"Hello");
    rclcpp::shutdown();
    return 0;

}