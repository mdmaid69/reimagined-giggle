import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)