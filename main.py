import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)