  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import array
def get_string_from_array(array):
        return array.tobytes()