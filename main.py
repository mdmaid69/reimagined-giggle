import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))