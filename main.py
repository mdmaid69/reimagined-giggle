import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))