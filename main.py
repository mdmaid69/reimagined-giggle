  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)