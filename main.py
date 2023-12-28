  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)