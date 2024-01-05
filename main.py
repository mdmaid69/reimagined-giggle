def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))