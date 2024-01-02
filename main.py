def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h