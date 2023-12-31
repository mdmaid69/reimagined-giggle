import array
def get_array_as_frozenset(array):
        return frozenset(array)
import glob
def find_files(pattern):
        return glob.glob(pattern)