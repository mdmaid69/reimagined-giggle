import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)