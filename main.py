import collections
def create_user_string():
        return collections.UserString()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)