import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)