import glob
def find_files(pattern):
        return glob.glob(pattern)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))