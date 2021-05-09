import unittest
import sys
import os.path
from socket import *
# import threading
import multiprocessing

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from options import *
from server import *
from client import *
from jim import *


class TestServerCase(unittest.TestCase):
    def setUp(self) -> None:
        self.thread = multiprocessing.Process(target=run, args=([], "../config_server.json"))
        self.thread.start()
        # self.thread = threading.Thread(target=run, args=([], "../config_server.json"))
        # self.thread.start()

    def test_run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 7777))
        msg = pack({"data": "test data"})
        sock.send(msg)
        msg = sock.recv(1024)
        print(unpack(msg))
        self.assertEqual(unpack(msg), {'response': 200, 'alert': 'Optional message / notification'},
                         "sending data error")
        sock.close()

    def tearDown(self) -> None:
        self.thread.terminate()


if __name__ == '__main__':
    unittest.main()
