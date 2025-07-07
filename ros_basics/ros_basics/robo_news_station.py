import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStation(Node):
    def __init__(self):
        super().__init__('news_node')
        self.publishers_ = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(1.0, self.publish_news)  # Call timer_callback every 1 second
        self.get_logger().info(f'New publish node has been created, publishing to "robot_news" topic every 1 second')
        self.declare_parameter('robot_name', 'default_name')

    def publish_news(self):  # when the method is called then it is published
        msg = String()  # Create a new String message
        msg.data = f"Hello, this is {self.get_parameter('robot_name').value} from the Robot News Station!"  # Set the message data
        self.publishers_.publish(msg)  # Publish the message
        self.get_logger().info(f'Published news: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation()
    rclpy.spin(node) # Keep the node alive until it is shut down
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()