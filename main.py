  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def pop_from_array(array, i=-1):
        return array.pop(i)