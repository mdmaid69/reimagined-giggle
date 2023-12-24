import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()