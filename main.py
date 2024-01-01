import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")