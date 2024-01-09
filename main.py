import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)