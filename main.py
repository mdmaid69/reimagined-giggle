def remove_duplicates(lst):
        return list(set(lst))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)