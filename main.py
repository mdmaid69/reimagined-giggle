import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_perpetuity(payment, rate):
        return payment / rate