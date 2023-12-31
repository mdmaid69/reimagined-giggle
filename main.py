import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)