  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import array
def get_bytes_from_array(array):
        return array.tobytes()