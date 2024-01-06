import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)