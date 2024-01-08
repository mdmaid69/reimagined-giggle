  import os
  def get_current_directory():
        return os.getcwd()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)