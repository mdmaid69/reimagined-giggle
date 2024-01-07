import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)