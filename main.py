import os
def list_files_in_directory(path):
        return os.listdir(path)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))