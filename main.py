import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True