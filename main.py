  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)