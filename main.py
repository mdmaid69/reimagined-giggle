  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result