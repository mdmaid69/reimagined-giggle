  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import array
def clear_array(array):
        array *= 0