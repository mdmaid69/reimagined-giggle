  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)