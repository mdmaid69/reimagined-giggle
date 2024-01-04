import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)