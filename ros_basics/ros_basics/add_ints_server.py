import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddIntsServer(Node):

    def __init__(self):
        super().__init__('add_ints_server')
        self.server = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info('Add Two Ints Service has been started.')
        # while deciding a name for the server, use 'verb' as it is an action, so it will do something like a computation or task.

    def add_two_ints_callback(self, request: AddTwoInts.Request, response: AddTwoInts.Response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Adding a = {str(request.a)}, b = {str(request.b)}, sum = {str(response.sum)}')
        # This is the callback function that will be called when a request is made to the service
        return response

def main(args=None):
    rclpy.init(args=args)
    add_ints_server = AddIntsServer()
    rclpy.spin(add_ints_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()