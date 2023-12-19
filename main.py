  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import array
def get_bytes_from_array(array):
        return array.tobytes()