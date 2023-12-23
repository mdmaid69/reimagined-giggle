  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)