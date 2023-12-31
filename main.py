  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import array
def get_bytes_from_array(array):
        return array.tobytes()