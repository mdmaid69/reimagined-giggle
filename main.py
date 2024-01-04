  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import array
def convert_array_to_bytes(array):
        return array.tobytes()