import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()