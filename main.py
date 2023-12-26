def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h