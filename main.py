import array
def clear_array(array):
        array *= 0
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink