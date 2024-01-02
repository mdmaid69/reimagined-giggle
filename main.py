import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)