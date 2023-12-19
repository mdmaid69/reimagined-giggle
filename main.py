import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)