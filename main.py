  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}