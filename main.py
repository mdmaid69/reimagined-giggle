import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import os
def get_environment_variable(var):
        return os.getenv(var)