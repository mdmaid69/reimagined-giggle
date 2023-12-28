def calculate_roi(gain, cost):
        return (gain - cost) / cost
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)