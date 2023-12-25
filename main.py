import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import os
def remove_directory(path):
        os.rmdir(path)