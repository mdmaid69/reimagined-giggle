import array
def get_array_length(array):
        return len(array)
  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino