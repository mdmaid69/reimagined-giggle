import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import glob
def find_files(pattern):
        return glob.glob(pattern)