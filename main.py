  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)