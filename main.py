def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)