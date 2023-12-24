  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result