import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)