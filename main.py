import array
def get_string_from_array(array):
        return array.tobytes()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)