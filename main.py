import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_perpetuity(payment, rate):
        return payment / rate