import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))