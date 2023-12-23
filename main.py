import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def find_difference(list1, list2):
        return set(list1) - set(list2)