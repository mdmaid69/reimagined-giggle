import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result