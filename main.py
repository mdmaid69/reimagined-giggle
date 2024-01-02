  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import array
def convert_array_to_bytes(array):
        return array.tobytes()