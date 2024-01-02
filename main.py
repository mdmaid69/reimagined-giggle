import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)