import os
def list_files_in_directory(path):
        return os.listdir(path)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))