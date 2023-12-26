import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import os
  def split_path(path):
        return os.path.split(path)