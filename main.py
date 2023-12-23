import array
def get_array_index(array, item):
        return array.index(item)
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev