import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)