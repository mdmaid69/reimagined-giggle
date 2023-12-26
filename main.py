import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)