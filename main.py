import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import glob
def find_files(pattern):
        return glob.glob(pattern)