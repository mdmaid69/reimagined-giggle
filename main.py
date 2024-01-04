  import sqlite3
  def close_database_connection(connection):
        connection.close()
import logging
def log_message(message):
        logging.info(message)