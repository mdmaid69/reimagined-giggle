import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns