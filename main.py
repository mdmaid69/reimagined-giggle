  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)