import os
def get_file_size(filename):
        return os.path.getsize(filename)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))