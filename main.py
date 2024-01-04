def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)