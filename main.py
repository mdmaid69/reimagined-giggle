  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import array
def convert_array_to_string(array):
        return array.tostring()