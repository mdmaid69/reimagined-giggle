import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_perpetuity(payment, rate):
        return payment / rate