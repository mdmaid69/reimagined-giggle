  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def convert_to_binary(n):
        return bin(n)