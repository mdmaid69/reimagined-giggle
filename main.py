  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def extend_array(array, iterable):
        array.extend(iterable)