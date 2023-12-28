def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)