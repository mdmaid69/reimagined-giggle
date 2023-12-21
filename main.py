  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import array
def get_string_from_array(array):
        return array.tobytes()