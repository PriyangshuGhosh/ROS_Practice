#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from personal_interface.srv import LedPanelState
from personal_interface.msg import LedPannel

class Led_Panel_node(Node):
    def __init__(self):
        super().__init__("LedPanelNode")
        self.led_pos_ = [0,0,0]
        self.service_ = self.create_service(LedPanelState,"set_led",self.caller)
        self.publisher_ = self.create_publisher(LedPannel,"set_led",10)
        self.create_timer(1.0,self.publish_state)
    def caller(self,request:LedPanelState.Request ,response:LedPanelState.Response):
        self.led_pos_[2]=int(request.state)
        self.get_logger().info(f"Received request {request.state} setting led pannel board to {self.led_pos_}")
        response.pannel=self.led_pos_
        return response 
    def publish_state(self):
        msg=LedPannel()
        msg.panel=self.led_pos_
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=Led_Panel_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()



