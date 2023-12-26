import sys
def print_python_version():
        print(sys.version)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))