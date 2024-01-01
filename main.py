import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)