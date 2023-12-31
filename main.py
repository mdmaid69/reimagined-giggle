import array
def get_array_itemsize(array):
        return array.itemsize
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)