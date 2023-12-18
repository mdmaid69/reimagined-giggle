import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)