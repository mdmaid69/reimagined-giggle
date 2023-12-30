import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result