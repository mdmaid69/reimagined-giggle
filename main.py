  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def convert_array_to_bytes(array):
        return array.tobytes()