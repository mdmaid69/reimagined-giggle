text = "Hello, world!"
print("Words:", len(text.split()))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h