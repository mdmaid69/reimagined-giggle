import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)