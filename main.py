import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)