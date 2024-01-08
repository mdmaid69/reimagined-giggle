  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)