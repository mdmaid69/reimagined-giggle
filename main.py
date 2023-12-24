import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)