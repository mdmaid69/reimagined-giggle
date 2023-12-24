import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import glob
def find_files(pattern):
        return glob.glob(pattern)