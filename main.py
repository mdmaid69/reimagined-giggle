import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)