  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)