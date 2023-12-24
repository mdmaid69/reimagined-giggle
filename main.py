n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)