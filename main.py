import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def delete_file(file_name):
        os.remove(file_name)