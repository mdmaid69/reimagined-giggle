import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)