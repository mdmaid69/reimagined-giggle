def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)