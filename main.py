  import os
  def get_base_name(path):
        return os.path.basename(path)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)