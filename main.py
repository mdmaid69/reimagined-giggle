  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)