import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import shutil
def move_file(src, dst):
        shutil.move(src, dst)