import glob
def find_files(pattern):
        return glob.glob(pattern)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)