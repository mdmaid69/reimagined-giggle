import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev