import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def greet(name):
        print(f"Hello, {name}!")