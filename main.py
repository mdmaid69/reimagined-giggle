  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)