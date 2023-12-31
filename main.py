def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))