import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))