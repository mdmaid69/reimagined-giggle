  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import array
def remove_from_array(array, item):
        array.remove(item)