import array
def get_array_as_bytearray(array):
        return bytearray(array)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)