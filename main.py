import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)