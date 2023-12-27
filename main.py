import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)