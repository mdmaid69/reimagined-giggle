import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)