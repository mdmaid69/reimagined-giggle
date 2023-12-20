  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import array
def clear_array(array):
        array *= 0