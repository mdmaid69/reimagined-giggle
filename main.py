def find_difference(list1, list2):
        return set(list1) - set(list2)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h