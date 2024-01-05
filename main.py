import array
def get_array_as_float(array):
        return float(array[0])
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime