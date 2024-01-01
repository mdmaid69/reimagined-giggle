import array
def get_array_index(array, item):
        return array.index(item)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)