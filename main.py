def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)