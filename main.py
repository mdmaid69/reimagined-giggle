  import os
  def get_current_directory():
        return os.getcwd()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)