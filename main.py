import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)