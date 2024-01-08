import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)