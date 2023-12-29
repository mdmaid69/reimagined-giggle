  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import array
def extend_array(array, iterable):
        array.extend(iterable)