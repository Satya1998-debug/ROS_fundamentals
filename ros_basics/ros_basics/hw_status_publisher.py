import rclpy
from rclpy.node import Node
from ros_interfaces.msg import HardwareStatus

class HwStatusPublisher(Node):
    def __init__(self):
        super().__init__('hw_status_publisher')
        self.publisher_ = self.create_publisher(HardwareStatus, 'hw_status', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.publish_hw_status)
        self.get_logger().info('hw_status_publisher node started ...')

    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 35.6
        msg.are_motors_operational = True
        msg.is_battery_operational = False
        msg.debug_message = f'Hardware status check SUCCESSFUL'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing hardware status: {str(msg.debug_message)}')

def main(args=None):
    rclpy.init(args=args)
    node = HwStatusPublisher()
    rclpy.spin(node)  # Keep the node alive until it is shut down
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()