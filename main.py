import array
def get_array_as_list(array):
        return list(array)
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize