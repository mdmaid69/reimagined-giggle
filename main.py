def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)