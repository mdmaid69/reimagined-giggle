  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import array
def get_array_index(array, item):
        return array.index(item)