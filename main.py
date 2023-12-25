import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import sklearn.datasets
print(sklearn.datasets.load_iris())