import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import sys
def print_python_version():
        return sys.version