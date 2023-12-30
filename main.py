  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)