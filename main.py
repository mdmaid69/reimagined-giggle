  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def get_bytes_from_array(array):
        return array.tobytes()