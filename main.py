import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import os
def change_working_directory(path):
        os.chdir(path)