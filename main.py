def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import collections
def count_elements(iterable):
        return collections.Counter(iterable)