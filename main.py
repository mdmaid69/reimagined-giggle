import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread