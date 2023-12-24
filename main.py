import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)