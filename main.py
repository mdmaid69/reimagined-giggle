import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")