import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)