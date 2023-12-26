  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)