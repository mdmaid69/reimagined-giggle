import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time