  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)