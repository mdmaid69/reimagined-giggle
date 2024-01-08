import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import os
def get_current_working_directory():
        return os.getcwd()