  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)