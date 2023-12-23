import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_work(force, distance):
        return force * distance