def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h