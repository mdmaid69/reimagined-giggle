  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import array
def get_bytes_from_array(array):
        return array.tobytes()