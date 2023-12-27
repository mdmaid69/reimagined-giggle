  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import array
def get_string_from_array(array):
        return array.tobytes()