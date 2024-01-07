  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import array
def get_array_buffer_info(array):
        return array.buffer_info()