  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result