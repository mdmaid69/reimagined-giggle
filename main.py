import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size