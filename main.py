import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time