import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result