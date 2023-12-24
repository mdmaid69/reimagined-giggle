import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def remove_duplicates(lst):
        return list(set(lst))