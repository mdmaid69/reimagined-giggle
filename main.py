  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import array
def get_array_index(array, item):
        return array.index(item)