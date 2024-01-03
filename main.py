import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time