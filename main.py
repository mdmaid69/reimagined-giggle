  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}