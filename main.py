import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)