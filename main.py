import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal