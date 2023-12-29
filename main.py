import logging
def log_message(message):
        logging.info(message)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)