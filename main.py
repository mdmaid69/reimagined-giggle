  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import array
def extend_array(array, iterable):
        array.extend(iterable)