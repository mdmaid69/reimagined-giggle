import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)