import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
i = 0
while i < 5:
        print(i)
        i += 1