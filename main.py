import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)