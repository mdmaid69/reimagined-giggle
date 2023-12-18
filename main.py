import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import sqlite3
  def close_database_connection(connection):
        connection.close()