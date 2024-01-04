  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def pop_from_array(array, i=-1):
        return array.pop(i)