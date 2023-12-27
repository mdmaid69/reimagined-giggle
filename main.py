  import sqlite3
  def close_database_connection(connection):
        connection.close()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()