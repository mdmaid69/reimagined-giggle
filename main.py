import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time