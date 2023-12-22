import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)