import array
def get_array_as_bytes(array):
        return bytes(array)
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime