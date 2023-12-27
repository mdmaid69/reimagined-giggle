import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import os
  def delete_file(file_name):
        os.remove(file_name)