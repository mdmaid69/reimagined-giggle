  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}