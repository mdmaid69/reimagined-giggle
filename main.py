import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import os
def get_file_size(filename):
        return os.path.getsize(filename)