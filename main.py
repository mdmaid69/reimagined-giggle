import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)