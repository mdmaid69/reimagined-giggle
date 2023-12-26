import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()