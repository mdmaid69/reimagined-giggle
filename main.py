import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid