import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size