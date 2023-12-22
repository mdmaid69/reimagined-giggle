import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)