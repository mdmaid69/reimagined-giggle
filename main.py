import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)