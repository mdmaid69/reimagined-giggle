  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import array
def get_array_as_tuple(array):
        return tuple(array)