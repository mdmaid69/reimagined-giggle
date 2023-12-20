import os
def get_environment_variable(var):
        return os.getenv(var)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))