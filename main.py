  import os
  def delete_file(file_name):
        os.remove(file_name)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)