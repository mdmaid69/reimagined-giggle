import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))