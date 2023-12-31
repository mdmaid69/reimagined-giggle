  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)