import array
def extend_array(array, iterable):
        array.extend(iterable)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)