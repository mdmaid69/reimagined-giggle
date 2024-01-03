import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time