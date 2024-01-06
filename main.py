import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def remove_duplicates(lst):
        return list(set(lst))