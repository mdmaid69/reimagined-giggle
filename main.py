import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def get_current_directory():
        return os.getcwd()