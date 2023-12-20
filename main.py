  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable