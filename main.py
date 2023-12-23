import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))