  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import array
def get_array_buffer_info(array):
        return array.buffer_info()