import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)