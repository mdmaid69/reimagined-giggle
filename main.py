import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time