import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)