import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import random
def generate_random_choice(choices):
        return random.choice(choices)