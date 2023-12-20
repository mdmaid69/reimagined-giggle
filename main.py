  import os
  def get_base_name(path):
        return os.path.basename(path)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)