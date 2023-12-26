import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)