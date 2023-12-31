import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def split_path(path):
        return os.path.split(path)