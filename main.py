def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)