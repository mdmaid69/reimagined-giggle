import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)