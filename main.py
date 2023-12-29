import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time