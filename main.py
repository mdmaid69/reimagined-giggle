  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import array
def get_bytes_from_array(array):
        return array.tobytes()