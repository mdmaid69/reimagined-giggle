  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import array
def extend_array(array, iterable):
        array.extend(iterable)