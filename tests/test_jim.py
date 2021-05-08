import sys
import os.path
import chardet
import unittest

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from jim import *


class TestJim(unittest.TestCase):
    def setUp(self) -> None:
        self.test_dict = {"data": "éâô"}
        self.test_str = "éâô"

    def test_pack(self):
        self.assertEqual(
            chardet.detect(pack(self.test_dict))["encoding"],
            "UTF-8-SIG", "encode type have to be utf-8-sig"
        )

    def test_unpack(self):
        test_str_msg = json.dumps(self.test_str)
        test_str_bytes = test_str_msg.encode("utf-8-sig")
        self.assertEqual(
            unpack(test_str_bytes), "éâô",
            "your message is packed in wrong way"
        )


if __name__ == '__main__':
    unittest.main()
