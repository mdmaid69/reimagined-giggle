import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import os
def change_working_directory(path):
        os.chdir(path)