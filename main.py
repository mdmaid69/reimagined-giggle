import array
def get_array_length(array):
        return len(array)
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid