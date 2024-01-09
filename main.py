  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import array
def get_bytes_from_array(array):
        return array.tobytes()