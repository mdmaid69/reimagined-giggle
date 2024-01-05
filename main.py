import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")