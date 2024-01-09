import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal