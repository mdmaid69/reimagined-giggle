  import sqlite3
  def close_database_connection(connection):
        connection.close()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")