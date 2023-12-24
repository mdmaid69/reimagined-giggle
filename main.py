import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import shutil
def delete_directory(path):
        shutil.rmtree(path)