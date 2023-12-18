import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)