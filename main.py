import json
def read_from_json(json_string):
        return json.loads(json_string)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")