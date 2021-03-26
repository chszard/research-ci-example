import unittest

import main

class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("HS TEST")
        self.assertEqual(ret, "hello world Ka")


if __name__ == "__main__":
    unittest.main()