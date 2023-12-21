  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)