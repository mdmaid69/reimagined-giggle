import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))