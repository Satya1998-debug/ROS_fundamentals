
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    
    node = Node('add_ints_client_no_oop')
    client = node.create_client(AddTwoInts, 'add_two_ints')  # same name of the client as the service

    while not client.wait_for_service(timeout_sec=1.0):  # if erver is UP this will exit the loop
        node.get_logger().warn('Service not available, waiting...')

    request = AddTwoInts.Request()
    request.a = 5
    request.b = 3

    future = client.call_async(request)

    rclpy.spin_until_future_complete(node, future)
    
    response = future.result()

    if response is not None:
        node.get_logger().info(f'a = {str(request.a)}, b = {str(request.b)} sent, got result sum = {str(response.sum)}')
    else:
        node.get_logger().error('Service call failed')

    rclpy.shutdown()
    