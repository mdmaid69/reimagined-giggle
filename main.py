import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)