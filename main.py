def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)