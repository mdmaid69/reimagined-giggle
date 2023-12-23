import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)