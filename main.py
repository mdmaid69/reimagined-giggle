import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]