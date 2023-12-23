  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result