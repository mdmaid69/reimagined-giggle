import logging
def log_message(message):
        logging.info(message)
  import sqlite3
  def close_database_connection(connection):
        connection.close()