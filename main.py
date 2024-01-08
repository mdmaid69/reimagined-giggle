import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)