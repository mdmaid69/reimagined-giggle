import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_perpetuity(payment, rate):
        return payment / rate