  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable