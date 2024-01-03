import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)