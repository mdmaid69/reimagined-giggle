n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)