import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import os
def get_current_working_directory():
        return os.getcwd()