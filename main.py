import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_volume(length, width, height):
        return length * width * height