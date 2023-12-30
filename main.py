  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import array
def get_string_from_array(array):
        return array.tobytes()