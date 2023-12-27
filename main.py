import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()