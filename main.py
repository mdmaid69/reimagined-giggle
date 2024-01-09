import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)