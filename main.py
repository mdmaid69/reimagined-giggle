  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)