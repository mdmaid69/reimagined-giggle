import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def calculate_volume(length, width, height):
        return length * width * height