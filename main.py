import array
def get_array_as_bytes(array):
        return bytes(array)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)