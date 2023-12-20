import array
def get_array_as_repr(array):
        return repr(array)
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns