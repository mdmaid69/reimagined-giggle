  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import array
def get_array_buffer_info(array):
        return array.buffer_info()