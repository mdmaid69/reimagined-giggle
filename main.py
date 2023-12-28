import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)