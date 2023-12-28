import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")