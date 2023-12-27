def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))