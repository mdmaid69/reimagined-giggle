import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)