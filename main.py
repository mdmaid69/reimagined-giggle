import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")