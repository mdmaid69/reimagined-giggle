def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)