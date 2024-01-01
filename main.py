import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")