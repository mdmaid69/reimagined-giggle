  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result