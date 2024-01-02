import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)