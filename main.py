import tensorflow as tf
print(tf.__version__)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)