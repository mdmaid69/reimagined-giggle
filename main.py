import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)