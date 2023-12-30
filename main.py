import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)