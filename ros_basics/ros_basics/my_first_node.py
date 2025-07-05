#!usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.counter = 0
        self.get_logger().info('Hello, ROS 2 Humble!')
        self.create_timer(1.0, self.timer_callback)  # we are registering the callback functions with the timer, we are not calling it directly

    def timer_callback(self):  # callback means call you back later ...analogy for understanding
        self.counter += 1
        self.get_logger().info(f'Hello! I am a Timer {self.counter}')


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) # Keep the node alive until it is shut down
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()