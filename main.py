  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}