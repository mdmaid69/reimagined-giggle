  import os
  def get_base_name(path):
        return os.path.basename(path)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)