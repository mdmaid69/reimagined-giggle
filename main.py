import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b