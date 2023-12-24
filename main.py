def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)