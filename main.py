  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)