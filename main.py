import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_perpetuity(payment, rate):
        return payment / rate