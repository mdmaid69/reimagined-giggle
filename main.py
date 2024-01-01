import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def split_path(path):
        return os.path.split(path)