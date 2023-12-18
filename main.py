  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result