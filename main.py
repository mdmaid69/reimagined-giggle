import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)