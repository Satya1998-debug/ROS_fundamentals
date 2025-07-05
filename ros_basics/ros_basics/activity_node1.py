
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberNode(Node):
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int64, 'number', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.publish_number)
        self.num = 1
        self.get_logger().info('number_publisher node started ...')    

    def publish_number(self):
        msg = Int64()
        msg.data = self.num
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing number: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberNode()
    rclpy.spin(node)  # Keep the node alive until it is shut down
    node.destroy_node()
    rclpy.shutdown()