  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)