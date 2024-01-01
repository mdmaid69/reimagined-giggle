  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def get_string_from_array(array):
        return array.tobytes()