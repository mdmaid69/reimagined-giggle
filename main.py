import array
def get_array_itemsize(array):
        return array.itemsize
  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode