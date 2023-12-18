import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
n = 10
print("Powers of 2:", [2**x for x in range(n)])