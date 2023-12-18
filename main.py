import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")