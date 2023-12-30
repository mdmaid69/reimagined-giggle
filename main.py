import array
def get_array_typecode(array):
        return array.typecode
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)