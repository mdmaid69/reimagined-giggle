import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def delete_file(file_name):
        os.remove(file_name)