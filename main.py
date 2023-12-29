import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b