import sklearn.datasets
print(sklearn.datasets.load_iris())
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")