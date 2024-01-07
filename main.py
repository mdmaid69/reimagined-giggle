  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")