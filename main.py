  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import array
def get_string_from_array(array):
        return array.tobytes()