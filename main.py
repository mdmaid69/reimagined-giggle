  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)