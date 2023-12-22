def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)