  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import array
def convert_array_to_bytes(array):
        return array.tobytes()