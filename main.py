  import os
  def delete_file(file_name):
        os.remove(file_name)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)