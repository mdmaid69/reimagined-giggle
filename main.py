import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def convert_to_octal(n):
        return oct(n)