def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))