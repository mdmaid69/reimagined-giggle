import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def split_path(path):
        return os.path.split(path)