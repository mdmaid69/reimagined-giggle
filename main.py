import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result