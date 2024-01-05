import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)