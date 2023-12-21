import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import os
def list_files_in_directory(path):
        return os.listdir(path)