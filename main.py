import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)