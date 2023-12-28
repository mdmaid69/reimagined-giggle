import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)