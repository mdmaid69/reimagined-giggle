  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)