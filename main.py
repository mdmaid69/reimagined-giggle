  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import array
def extend_array(array, iterable):
        array.extend(iterable)