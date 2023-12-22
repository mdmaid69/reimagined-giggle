  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import array
def get_array_slice(array, i, j):
        return array[i:j]