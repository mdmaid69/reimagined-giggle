  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import array
def get_array_buffer_info(array):
        return array.buffer_info()