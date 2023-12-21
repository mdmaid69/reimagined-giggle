import os
def remove_directory(path):
        os.rmdir(path)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))