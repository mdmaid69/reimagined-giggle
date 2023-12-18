import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import logging
def setup_logging(level):
        logging.basicConfig(level=level)