import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h