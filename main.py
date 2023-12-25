def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)