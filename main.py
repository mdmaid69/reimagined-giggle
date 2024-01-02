import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)