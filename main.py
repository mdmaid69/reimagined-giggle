import array
def get_array_itemsize(array):
        return array.itemsize
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)