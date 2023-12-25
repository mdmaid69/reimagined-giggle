import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)