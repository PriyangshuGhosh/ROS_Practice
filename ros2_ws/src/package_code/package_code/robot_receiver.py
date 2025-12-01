#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String 

class ReceiverNode(Node):
    def __init__(self):
        super().__init__("receiver")
        self.subscriber_= self.create_subscription(String ,"iterator_value",self.callback,10)

    def callback(self,msg:String):
        self.get_logger().info(f"Hello this received data : {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = ReceiverNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
