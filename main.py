  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import array
def get_array_item(array, i):
        return array[i]