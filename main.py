import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b