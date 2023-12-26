import array
def get_array_as_repr(array):
        return repr(array)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)