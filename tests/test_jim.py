import unittest
import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from client import *
from options import *


class TestClientCase(unittest.TestCase):
    def test_create_presence_msg(self):
        test_user_name = "Vasya Pupkin"
        test_status = "absent"
        self.assertEqual(
            type(create_presence_msg(test_user_name, test_status)), dict, "msg to send have to be in a dict form")
        print('hello')


if __name__ == '__main__':
    unittest.main()
