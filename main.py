def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)