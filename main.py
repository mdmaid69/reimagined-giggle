import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)