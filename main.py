  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)