  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}