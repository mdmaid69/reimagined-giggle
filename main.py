def find_unique_words(sentence):
        return set(sentence.split())
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")