import array
def get_array_as_bytes(array):
        return bytes(array)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)