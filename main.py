  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import array
def append_to_array(array, item):
        array.append(item)