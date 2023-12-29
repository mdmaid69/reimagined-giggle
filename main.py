import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result