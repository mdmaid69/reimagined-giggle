  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}