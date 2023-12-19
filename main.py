  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")