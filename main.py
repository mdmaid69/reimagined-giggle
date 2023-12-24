  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)