  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result