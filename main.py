import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)