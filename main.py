  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}