import os
def remove_directory(path):
        os.rmdir(path)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))