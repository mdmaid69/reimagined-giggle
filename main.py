  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)