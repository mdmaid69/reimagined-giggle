  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import array
def get_bytes_from_array(array):
        return array.tobytes()