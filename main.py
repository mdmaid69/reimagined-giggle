import datetime
def get_current_datetime():
        return datetime.datetime.now()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")