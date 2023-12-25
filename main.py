import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")