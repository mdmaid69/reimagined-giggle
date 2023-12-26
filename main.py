import array
def get_bytes_from_array(array):
        return array.tobytes()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)