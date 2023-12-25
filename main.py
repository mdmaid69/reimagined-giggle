import os
def change_working_directory(path):
        os.chdir(path)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))