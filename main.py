import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result