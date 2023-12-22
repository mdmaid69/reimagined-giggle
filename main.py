  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)