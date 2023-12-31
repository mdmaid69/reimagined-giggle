import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time