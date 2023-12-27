def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)