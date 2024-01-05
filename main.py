import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import os
def get_current_working_directory():
        return os.getcwd()