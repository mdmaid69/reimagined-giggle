import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)