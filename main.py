import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)