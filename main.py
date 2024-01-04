  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)