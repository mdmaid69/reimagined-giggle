  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import array
def clear_array(array):
        array *= 0