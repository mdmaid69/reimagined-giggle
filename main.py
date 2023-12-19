import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)