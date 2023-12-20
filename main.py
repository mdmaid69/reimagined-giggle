import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]