sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")