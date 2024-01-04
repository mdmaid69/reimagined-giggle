import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time