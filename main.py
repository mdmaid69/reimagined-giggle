import sys
def print_python_version():
        print(sys.version)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))