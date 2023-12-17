import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)