import array
def get_array_as_bytearray(array):
        return bytearray(array)
  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid