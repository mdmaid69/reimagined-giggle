import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)