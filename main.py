  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def get_bytes_from_array(array):
        return array.tobytes()