  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)