#! usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Robot_transmitter(Node):
    def __init__(self):
        super().__init__("Robot_data")
        self.counter = 0  
        self.timer_ = self.create_timer(1.0, self.publish_callback)
        self.publisher_ = self.create_publisher(String, "iterator_value", 1)
        self.get_logger().info("Data transmitting..\n")

    def publish_callback(self):
        msg = String()
        msg.data = f"Iterator value : {self.counter}"
        self.publisher_.publish(msg)
        self.counter += 1
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = Robot_transmitter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
