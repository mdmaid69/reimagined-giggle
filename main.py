  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def convert_array_to_bytes(array):
        return array.tobytes()