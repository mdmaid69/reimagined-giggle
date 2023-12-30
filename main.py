import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))