import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()