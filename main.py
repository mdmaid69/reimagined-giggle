  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result