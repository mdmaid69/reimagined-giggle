import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")