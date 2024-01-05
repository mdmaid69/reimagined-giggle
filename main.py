def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")