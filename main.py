  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}