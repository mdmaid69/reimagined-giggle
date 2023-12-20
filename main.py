import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def find_common_elements(list1, list2):
        return set(list1) & set(list2)