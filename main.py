  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)