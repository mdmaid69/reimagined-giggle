  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import array
def pop_from_array(array, i=-1):
        return array.pop(i)