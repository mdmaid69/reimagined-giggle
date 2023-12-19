  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)