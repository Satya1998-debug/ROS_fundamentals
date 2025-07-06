
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from rcl_interfaces.msg import SetParametersResult

class NumberNode(Node):
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int64, 'number', 10)
        self.declare_parameter('timer_period', 2.0)
        self.declare_parameter('number', 1)
        self.timer_period_ = self.get_parameter('timer_period').value
        self.timer = self.create_timer(self.timer_period_, self.publish_number)
        self.num_ = self.get_parameter('number').value
        self.get_logger().info('number_publisher node started ...')  
        
        # parameter callback
        self.add_on_set_parameters_callback(self.parameter_callback)
        
    def parameter_callback(self, params: list[rclpy.parameter.Parameter]):
        for param in params:
            if param.name == 'number':
                self.num_ = param.value
                self.get_logger().info(f'Parameter "number" updated to: {str(self.num_)}')
        return SetParametersResult(successful=True)

    def publish_number(self):
        msg = Int64()
        msg.data = self.num_
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing number: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberNode()
    rclpy.spin(node)  # Keep the node alive until it is shut down
    node.destroy_node()
    rclpy.shutdown()