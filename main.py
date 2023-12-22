import array
def get_array_as_frozenset(array):
        return frozenset(array)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)