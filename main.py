import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)