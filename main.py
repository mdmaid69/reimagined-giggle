  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def remove_from_array(array, item):
        array.remove(item)