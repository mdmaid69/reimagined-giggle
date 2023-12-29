  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)