import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64  

class NumberPublisher(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.counter_=0
        self.timer = self.create_timer(1.0, self.callback)  
        self.publisher_ = self.create_publisher(Int64, "number", 1)
        self.get_logger().info("Publisher started transmitting numbers of type Int64")

    def callback(self):
        num = Int64()
        num.data = self.counter_
        self.publisher_.publish(num)
        self.get_logger().info(f"Published: {num.data}")
        self.counter_+=1


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
