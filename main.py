  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import array
def reverse_array(array):
        array.reverse()