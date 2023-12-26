import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b