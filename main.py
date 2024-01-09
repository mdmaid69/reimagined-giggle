  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import array
def get_bytes_from_array(array):
        return array.tobytes()