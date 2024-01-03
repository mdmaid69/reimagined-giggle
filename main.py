  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result