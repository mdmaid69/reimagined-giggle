import os
def remove_directory(path):
        os.rmdir(path)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))