  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)