  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import array
def convert_array_to_bytes(array):
        return array.tobytes()