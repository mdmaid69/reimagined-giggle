  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}