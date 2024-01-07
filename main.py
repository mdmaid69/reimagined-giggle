import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))