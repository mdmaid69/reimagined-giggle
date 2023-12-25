import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()