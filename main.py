import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)