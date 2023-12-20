import array
def get_bytes_from_array(array):
        return array.tobytes()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)