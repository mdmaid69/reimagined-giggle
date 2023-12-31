import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
text = "Hello, world!"
print("Characters:", len(text))