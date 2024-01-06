import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)