  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)