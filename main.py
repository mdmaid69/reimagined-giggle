  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)