  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}