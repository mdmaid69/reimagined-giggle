import array
def get_array_as_bool(array):
        return bool(array)
  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid