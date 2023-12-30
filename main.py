  import sqlite3
  def close_database_connection(connection):
        connection.close()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")