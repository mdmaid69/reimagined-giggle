import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")