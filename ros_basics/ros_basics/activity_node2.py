
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__('number_counter')
        self.subscriber_ = self.create_subscription(Int64, 'number', self.callback_number, 10)
        self.publisher_ = self.create_publisher(Int64, 'number_count', 10)
        
        # creating server 
        self.reset_server_ = self.create_service(SetBool, 'reset_counter', self.reset_counter_callback)
        self.get_logger().info('Reset counter service created.')

        self.num_counter = 0
        self.get_logger().info('number_counter node started ...., this is a subscriber and a publisher.')
        
    def reset_counter_callback(self, request: SetBool.Request, response: SetBool.Response):
        if request.data:
            self.num_counter = 0
            self.get_logger().info(f'Counter reset success. Counter is now {self.num_counter}.')
            response.success = True
        else:
            self.get_logger().info(f'Counter reset failed, request was not true.')
            response.success = False
        return response

    def callback_number(self, msg):
        self.get_logger().info(f'Received: {msg.data}')
        self.num_counter += 1
        self.get_logger().info(f'Number of messages received so far: {self.num_counter}')
        self.publish_number_count()

    def publish_number_count(self):
        msg = Int64()
        msg.data = self.num_counter
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing number count: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)  # Keep the node alive until it is shut down
    node.destroy_node()
    rclpy.shutdown()