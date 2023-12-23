import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")