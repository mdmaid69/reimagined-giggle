def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)