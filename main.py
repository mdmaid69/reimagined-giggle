  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)