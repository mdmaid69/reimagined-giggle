import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import os
def get_environment_variable(var):
        return os.getenv(var)