  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()