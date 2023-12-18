import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))