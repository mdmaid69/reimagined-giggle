import collections
def create_counter():
        return collections.Counter()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time