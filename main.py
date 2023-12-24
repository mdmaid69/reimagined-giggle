import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))