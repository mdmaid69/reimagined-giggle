  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)