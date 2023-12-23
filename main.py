import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import os
def get_file_size(filename):
        return os.path.getsize(filename)