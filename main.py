import os
def change_working_directory(path):
        os.chdir(path)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))