import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)