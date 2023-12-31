import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)