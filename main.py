  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import array
def get_array_as_float(array):
        return float(array[0])