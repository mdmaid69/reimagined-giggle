def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)