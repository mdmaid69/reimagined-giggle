  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def get_bytes_from_array(array):
        return array.tobytes()