import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys

class AddTwoIntsClient(Node):

    def __init__(self):
        super().__init__('add_two_ints_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    if len(sys.argv) != 3:
        AddTwoIntsClient.get_logger().info('Usage: add_two_ints_client <arg1> <arg2>')
        return
    
    add_two_ints_client = AddTwoIntsClient()
    add_two_ints_client.send_request(int(sys.argv[1]), int(sys.argv[2]))

    while rclpy.ok():
        rclpy.spin_once(add_two_ints_client)
        if add_two_ints_client.future.done():
            try:
                response = add_two_ints_client.future.result()
            except Exception as e:
                add_two_ints_client.get_logger().error(f'Service call failed: {e}')
            else:
                add_two_ints_client.get_logger().info(f'Result of add_two_ints: {response.sum}')
            break
    
    add_two_ints_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
