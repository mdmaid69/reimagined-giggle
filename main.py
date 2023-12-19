import array
def get_array_as_str(array):
        return str(array)
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid