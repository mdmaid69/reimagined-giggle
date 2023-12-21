  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)