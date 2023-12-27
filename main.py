import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)