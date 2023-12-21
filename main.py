import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)