  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import array
def pop_from_array(array, i=-1):
        return array.pop(i)