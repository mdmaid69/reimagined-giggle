import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)