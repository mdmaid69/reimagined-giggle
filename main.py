  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import array
def reverse_array(array):
        array.reverse()