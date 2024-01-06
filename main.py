  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)