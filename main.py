import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import glob
def find_files(pattern):
        return glob.glob(pattern)