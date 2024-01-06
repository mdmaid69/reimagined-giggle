import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import shutil
def delete_directory(path):
        shutil.rmtree(path)