import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()