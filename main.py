import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result