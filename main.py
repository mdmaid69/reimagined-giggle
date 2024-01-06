import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)