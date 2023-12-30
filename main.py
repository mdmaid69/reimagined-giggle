import array
def get_string_from_array(array):
        return array.tobytes()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)