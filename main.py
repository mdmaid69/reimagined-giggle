import array
def get_array_slice(array, i, j):
        return array[i:j]
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns