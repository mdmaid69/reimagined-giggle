  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)