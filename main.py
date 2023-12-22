import sys
def exit_program():
        sys.exit()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))