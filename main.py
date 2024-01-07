  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)