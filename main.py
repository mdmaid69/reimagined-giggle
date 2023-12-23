import glob
def find_files(pattern):
        return glob.glob(pattern)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)