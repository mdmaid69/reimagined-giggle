import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list