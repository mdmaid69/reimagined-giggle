def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)