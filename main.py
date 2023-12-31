import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()