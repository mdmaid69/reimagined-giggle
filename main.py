import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)