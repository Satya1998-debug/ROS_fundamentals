import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddIntsClients(Node):
    
    def __init__(self):
        super().__init__('add_ints_client')
        self.client_ = self.create_client(AddTwoInts, 'add_two_ints')
        self.get_logger().info('Add Two Ints Client has been started.')

    def call_add_ints(self, a, b):
        while not self.client_.wait_for_service(timeout_sec=1.0):  # if server is UP this will exit the loop
            self.get_logger().warn('Service not available, waiting...')
            
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
            
        future = self.client_.call_async(request)
        future.add_done_callback(self.callback_add_ints)
        
    def callback_add_ints(self, future):
        response = future.result()
        self.get_logger().info(f"Got response, sum = {str(response.sum)}")

def main(args=None):
    rclpy.init(args=args)
    node = AddIntsClients()
    node.call_add_ints(10, 15)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()