  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result