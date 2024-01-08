import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)