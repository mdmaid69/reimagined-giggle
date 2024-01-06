  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)