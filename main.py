import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)