import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)