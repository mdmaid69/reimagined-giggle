  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import array
def get_bytes_from_array(array):
        return array.tobytes()