import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)