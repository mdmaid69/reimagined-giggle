  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)