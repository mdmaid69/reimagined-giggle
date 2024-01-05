  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import array
def get_string_from_array(array):
        return array.tobytes()