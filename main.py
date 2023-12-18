import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result