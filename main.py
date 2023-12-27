import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)