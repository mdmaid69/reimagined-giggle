def find_union(list1, list2):
        return set(list1) | set(list2)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)