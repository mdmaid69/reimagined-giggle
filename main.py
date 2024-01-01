import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_volume(length, width, height):
        return length * width * height