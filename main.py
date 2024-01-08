def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)