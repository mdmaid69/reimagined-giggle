  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)