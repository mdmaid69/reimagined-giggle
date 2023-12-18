  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}