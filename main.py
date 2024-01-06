  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)