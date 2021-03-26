import unittest

import main

class MainTest(unittest.TestCase):
    def test_helloworld(self):
        result = main.helloworld("HS TEST")
        self.assertEqual(result, "hello world Ka")


if __name__ == "__main__":
    unittest.main()