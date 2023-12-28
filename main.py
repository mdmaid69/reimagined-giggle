import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)