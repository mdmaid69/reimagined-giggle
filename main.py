import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def greet(name):
        print(f"Hello, {name}!")