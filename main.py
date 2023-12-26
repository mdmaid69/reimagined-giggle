import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)