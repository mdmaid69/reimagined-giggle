def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))