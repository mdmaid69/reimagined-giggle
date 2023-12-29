import os
def list_files_in_directory(path):
        return os.listdir(path)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))