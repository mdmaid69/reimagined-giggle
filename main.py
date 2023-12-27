import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)