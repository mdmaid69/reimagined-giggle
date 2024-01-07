import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result