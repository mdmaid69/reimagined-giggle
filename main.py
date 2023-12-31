import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_work(force, distance):
        return force * distance