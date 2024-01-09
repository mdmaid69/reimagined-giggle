  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import array
def extend_array(array, iterable):
        array.extend(iterable)