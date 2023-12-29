  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)