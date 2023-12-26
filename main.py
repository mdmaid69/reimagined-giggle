import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)