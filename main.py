  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import array
def get_array_as_float(array):
        return float(array[0])