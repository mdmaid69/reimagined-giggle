import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def sort_list(lst):
        return sorted(lst)