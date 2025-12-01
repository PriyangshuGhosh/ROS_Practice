#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from personal_interface.srv import LedPanelState
from functools import partial

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery_node")
        self.battery_state_=True
        self.delays = [4.0, 6.0] 
        self.step = 0
        self.client_=self.create_client(LedPanelState,"set_led")
        self.get_logger().info("Battery Node started")
        self.schedule_next()
        
    def schedule_next(self):
        current_delay = self.delays[self.step % 2]
        self.timer = self.create_timer(current_delay, self.callback)

    def callback(self):
        self.timer.cancel() 

        self.step += 1
        self.battery_state_ = not self.battery_state_

        if not self.client_.wait_for_service(2.0):
            self.get_logger().warn("Waiting for server to be online")
            self.schedule_next()
            return
        
        request=LedPanelState.Request()
        request.state = self.battery_state_
        future = self.client_.call_async(request)
        future.add_done_callback(partial(self.callback2, request=request))
        

    def callback2(self,future,request):
            response = future.result()
            if response.pannel[2]:
                 self.get_logger().info("The battery is low.")
            else:
                 self.get_logger().info("The battery is full.")
            self.schedule_next()
            
def main(args=None):
     rclpy.init(args=args)
     node=BatteryNode()
     rclpy.spin(node)
     rclpy.shutdown()

if __name__ == "__main__":
     main()
