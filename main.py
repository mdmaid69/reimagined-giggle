import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)