import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)