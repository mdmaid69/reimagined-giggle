import sys
def add_to_python_path(path):
        sys.path.append(path)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")