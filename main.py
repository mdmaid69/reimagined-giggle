  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}