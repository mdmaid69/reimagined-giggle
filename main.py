  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)