  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)