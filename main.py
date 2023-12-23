  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)