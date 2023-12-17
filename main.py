import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time