import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()