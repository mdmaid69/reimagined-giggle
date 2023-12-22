  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import array
def clear_array(array):
        array *= 0