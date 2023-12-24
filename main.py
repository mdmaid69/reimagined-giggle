  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result