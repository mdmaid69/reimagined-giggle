import array
def set_array_item(array, i, item):
        array[i] = item
  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino