import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)