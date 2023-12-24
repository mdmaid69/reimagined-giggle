import os
def get_file_size(filename):
        return os.path.getsize(filename)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))