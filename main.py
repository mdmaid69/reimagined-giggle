import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)