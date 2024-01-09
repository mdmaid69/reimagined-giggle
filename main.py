import collections
def create_queue():
        return collections.deque()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()