  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import array
def get_array_buffer_info(array):
        return array.buffer_info()