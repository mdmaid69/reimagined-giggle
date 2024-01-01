import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)